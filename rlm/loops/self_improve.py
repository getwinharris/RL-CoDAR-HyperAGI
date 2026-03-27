"""
Self-Improving RLM Loop
Combines RLM infinite context with HyperAgents self-improvement
"""

import os
import json
from typing import Dict, List, Tuple
from rlm import RLM
from rlm.datasets.stream_datasets import DatasetStreamer, ByteDatasetTokenizer
from rlm.agents.hyper.meta_agent import MetaAgent
from rlm.agents.hyper.task_agent import TaskAgent


class SelfImprovingRLM:
    """
    Self-improving RLM that:
    1. Streams datasets to REPL (infinite context)
    2. Uses byte-level tokenization (0-255)
    3. Generates code patches via Meta-Agent
    4. Evaluates patches via Task-Agent
    5. Applies best patches to improve
    """
    
    def __init__(
        self,
        backend: str = "openai",
        backend_kwargs: Dict = None,
        dataset_name: str = "fineweb",
        max_iterations: int = 100,
        output_dir: str = "./outputs"
    ):
        """
        Args:
            backend: LLM backend (openai, anthropic, etc.)
            backend_kwargs: Backend configuration
            dataset_name: Dataset to stream (fineweb, finewiki, the-stack)
            max_iterations: Maximum self-improvement iterations
            output_dir: Directory for outputs
        """
        self.rlm = RLM(
            backend=backend,
            backend_kwargs=backend_kwargs or {"model_name": "gpt-4o"},
            persistent=True,  # Reuse REPL across iterations
            max_iterations=max_iterations
        )
        
        self.dataset = DatasetStreamer(dataset_name)
        self.tokenizer = ByteDatasetTokenizer()
        
        self.meta_agent = MetaAgent()
        self.task_agent = TaskAgent()
        
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
        # Tracking
        self.archive = []  # Store all iterations
        self.current_gen = 0  # Current generation
    
    def improve_step(self) -> Tuple[Dict, str]:
        """
        One step of self-improvement
        
        Returns:
            Tuple of (scores, best_patch)
        """
        print(f"\n{'='*60}")
        print(f"Self-Improvement Iteration {self.current_gen}")
        print(f"{'='*60}")
        
        # Step 1: Stream new context from dataset
        print("\n[1/5] Streaming dataset to REPL...")
        context_var = f"context_{self.current_gen}"
        context_code = next(self.dataset.stream_to_repl(context_var))
        
        # Execute in REPL to load context
        self.rlm._persistent_env.execute(context_code)
        print(f"✓ Loaded {context_var} into REPL")
        
        # Step 2: RLM analyzes with infinite context
        print("\n[2/5] Analyzing context with RLM...")
        analysis_prompt = f"""
Analyze the streamed context in {context_var}.

Tasks:
1. Identify patterns and insights
2. Find areas for improvement
3. Suggest specific code modifications
4. Preserve all key information

Context: {context_var}
"""
        analysis = self.rlm.completion(analysis_prompt)
        print(f"✓ Analysis complete ({len(analysis.response)} chars)")
        
        # Step 3: Meta-Agent generates code patches
        print("\n[3/5] Generating code patches...")
        patches = self.meta_agent.forward(
            repo_path=os.path.dirname(os.path.dirname(__file__)),
            eval_path=self.output_dir,
            analysis=analysis.response
        )
        print(f"✓ Generated {len(patches)} patches")
        
        # Step 4: Task-Agent evaluates patches
        print("\n[4/5] Evaluating patches...")
        scores = {}
        for patch_idx, patch in enumerate(patches):
            eval_input = {
                "domain": "code_improvement",
                "patch": patch,
                "analysis": analysis.response,
                "context": context_var
            }
            prediction, _ = self.task_agent.forward(eval_input)
            scores[patch_idx] = self._extract_score(prediction)
            print(f"  Patch {patch_idx}: score={scores[patch_idx]}")
        
        # Step 5: Apply best patch
        print("\n[5/5] Applying best patch...")
        best_patch_idx = max(scores, key=scores.get)
        best_patch = patches[best_patch_idx]
        self._apply_patch(best_patch)
        print(f"✓ Applied patch {best_patch_idx} (score={scores[best_patch_idx]})")
        
        # Archive results
        iteration_data = {
            "gen": self.current_gen,
            "context_var": context_var,
            "analysis_length": len(analysis.response),
            "num_patches": len(patches),
            "scores": scores,
            "best_patch_idx": best_patch_idx,
            "best_score": scores[best_patch_idx]
        }
        self.archive.append(iteration_data)
        self._save_archive()
        
        self.current_gen += 1
        
        return scores, best_patch
    
    def _extract_score(self, prediction: str) -> float:
        """Extract score from task agent prediction"""
        try:
            # Try to parse JSON
            if "{" in prediction:
                start = prediction.index("{")
                end = prediction.rindex("}") + 1
                json_str = prediction[start:end]
                data = json.loads(json_str)
                return float(data.get("score", 0.5))
        except:
            pass
        
        # Default score
        return 0.5
    
    def _apply_patch(self, patch: str) -> bool:
        """Apply code patch to repository"""
        # TODO: Implement patch application
        # For now, just save the patch
        patch_file = os.path.join(self.output_dir, f"gen_{self.current_gen}.patch")
        with open(patch_file, "w") as f:
            f.write(patch)
        return True
    
    def _save_archive(self):
        """Save archive to disk"""
        archive_file = os.path.join(self.output_dir, "archive.json")
        with open(archive_file, "w") as f:
            json.dump(self.archive, f, indent=2)
    
    def run(self, num_iterations: int = None):
        """
        Run self-improvement loop
        
        Args:
            num_iterations: Number of iterations (None for max_iterations)
        """
        iterations = num_iterations or self.rlm.max_iterations
        
        print(f"\n{'='*60}")
        print(f"Starting Self-Improving RLM")
        print(f"  Dataset: {self.dataset.dataset_name}")
        print(f"  Backend: {self.rlm.backend}")
        print(f"  Iterations: {iterations}")
        print(f"  Output: {self.output_dir}")
        print(f"{'='*60}")
        
        for i in range(iterations):
            try:
                scores, patch = self.improve_step()
                print(f"\n✓ Iteration {i+1}/{iterations} complete")
                print(f"  Best score: {max(scores.values()):.3f}")
                
            except KeyboardInterrupt:
                print("\n\n⚠️  Interrupted by user")
                break
            except Exception as e:
                print(f"\n❌ Error in iteration {i+1}: {e}")
                continue
        
        print(f"\n{'='*60}")
        print(f"Self-improvement complete!")
        print(f"  Total iterations: {self.current_gen}")
        print(f"  Archive saved to: {self.output_dir}/archive.json")
        print(f"{'='*60}")
        
        return self.archive


# Example usage
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Self-Improving RLM")
    parser.add_argument("--backend", type=str, default="openai")
    parser.add_argument("--model", type=str, default="gpt-4o")
    parser.add_argument("--dataset", type=str, default="fineweb")
    parser.add_argument("--iterations", type=int, default=10)
    parser.add_argument("--output", type=str, default="./outputs")
    
    args = parser.parse_args()
    
    rlm = SelfImprovingRLM(
        backend=args.backend,
        backend_kwargs={"model_name": args.model},
        dataset_name=args.dataset,
        max_iterations=args.iterations,
        output_dir=args.output
    )
    
    rlm.run()
