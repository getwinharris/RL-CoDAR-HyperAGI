"""
Dataset Streaming for RLM
Stream datasets to REPL variables without downloading
"""

from datatrove.pipeline.readers import ParquetReader
from datasets import load_dataset
from typing import Generator, Union, Dict, List


class DatasetStreamer:
    """Stream datasets to RLM REPL as context variables"""
    
    def __init__(self, dataset_name: str, split: str = None, limit: int = None):
        """
        Args:
            dataset_name: HuggingFace dataset name or path
            split: Dataset split (train, test, etc.)
            limit: Limit number of documents (None for all)
        """
        self.dataset_name = dataset_name
        self.split = split
        self.limit = limit
        self.count = 0
    
    def stream_fineweb(self) -> Generator[Dict, None, None]:
        """Stream FineWeb dataset (parquet format)"""
        # Stream from HF without downloading
        reader = ParquetReader("hf://datasets/HuggingFaceFW/fineweb/data")
        
        for document in reader():
            if self.limit and self.count >= self.limit:
                break
            self.count += 1
            yield {
                "text": document.get("text", ""),
                "id": document.get("id", ""),
                "source": "fineweb"
            }
    
    def stream_finewiki(self) -> Generator[Dict, None, None]:
        """Stream FineWiki dataset"""
        ds = load_dataset("HuggingFaceFW/finewiki", split=self.split)
        
        for item in ds:
            if self.limit and self.count >= self.limit:
                break
            self.count += 1
            yield {
                "text": item.get("text", ""),
                "title": item.get("title", ""),
                "source": "finewiki"
            }
    
    def stream_the_stack(self) -> Generator[Dict, None, None]:
        """Stream The-Stack v2 code dataset"""
        ds = load_dataset("bigcode/the-stack-v2")
        
        for file in ds:
            if self.limit and self.count >= self.limit:
                break
            self.count += 1
            yield {
                "code": file.get("content", ""),
                "path": file.get("path", ""),
                "language": file.get("language", ""),
                "source": "the-stack"
            }
    
    def stream_to_repl(self, var_name: str = "context") -> Generator[str, None, None]:
        """
        Stream dataset to RLM REPL as context variable
        
        Args:
            var_name: Variable name in REPL (context_0, context_1, etc.)
            
        Yields:
            Python code to add context to REPL
        """
        if "fineweb" in self.dataset_name:
            stream = self.stream_fineweb()
        elif "finewiki" in self.dataset_name:
            stream = self.stream_finewiki()
        elif "stack" in self.dataset_name:
            stream = self.stream_the_stack()
        else:
            raise ValueError(f"Unknown dataset: {self.dataset_name}")
        
        for i, doc in enumerate(stream):
            # Generate Python code to add to REPL
            code = f"""
# Streamed document {i} from {self.dataset_name}
{var_name}_{i} = {repr(doc)}
"""
            yield code


class ByteDatasetTokenizer:
    """
    Byte-level tokenizer for omni-model
    Vocabulary: 0-255 (fixed, no training needed)
    """
    
    def __init__(self):
        self.vocab_size = 256
        self.eos_token = 255  # Use last byte as EOS
    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to byte sequence (0-255)
        
        Args:
            text: Input text
            
        Returns:
            List of byte values
        """
        return [b for b in text.encode('utf-8')]
    
    def decode(self, byte_sequence: List[int]) -> str:
        """
        Convert byte sequence back to text
        
        Args:
            byte_sequence: List of byte values (0-255)
            
        Returns:
            Decoded text
        """
        return bytes(byte_sequence).decode('utf-8')
    
    def encode_dataset(self, dataset_stream: Generator[Dict, None, None]) -> Generator[List[int], None, None]:
        """
        Encode entire dataset as byte sequences
        
        Args:
            dataset_stream: Generator of documents
            
        Yields:
            Byte sequences
        """
        for doc in dataset_stream:
            text = doc.get("text", doc.get("code", ""))
            yield self.encode(text)
    
    def get_stats(self, dataset_stream: Generator[Dict, None, None]) -> Dict:
        """
        Get byte distribution statistics
        
        Args:
            dataset_stream: Generator of documents
            
        Returns:
            Statistics dictionary
        """
        byte_counts = [0] * 256
        total_bytes = 0
        
        for doc in dataset_stream:
            text = doc.get("text", doc.get("code", ""))
            bytes_seq = self.encode(text)
            total_bytes += len(bytes_seq)
            
            for b in bytes_seq:
                byte_counts[b] += 1
        
        # Find most/least common bytes
        most_common = max(range(256), key=lambda i: byte_counts[i])
        least_common = min(range(256), key=lambda i: byte_counts[i])
        
        return {
            "total_bytes": total_bytes,
            "vocab_size": self.vocab_size,
            "most_common_byte": most_common,
            "most_common_count": byte_counts[most_common],
            "least_common_byte": least_common,
            "least_common_count": byte_counts[least_common],
            "avg_bytes_per_doc": total_bytes / max(1, self.count if hasattr(self, 'count') else 1)
        }


# Example usage
if __name__ == "__main__":
    # Stream FineWeb
    streamer = DatasetStreamer("fineweb", limit=10)
    
    tokenizer = ByteDatasetTokenizer()
    
    print("Streaming and tokenizing FineWeb dataset...")
    stats = tokenizer.get_stats(streamer.stream_fineweb())
    
    print(f"\nDataset Statistics:")
    print(f"  Total bytes: {stats['total_bytes']:,}")
    print(f"  Vocab size: {stats['vocab_size']} (fixed)")
    print(f"  Most common byte: {stats['most_common_byte']} ({stats['most_common_count']:,} occurrences)")
    print(f"  Average bytes/doc: {stats['avg_bytes_per_doc']:,.0f}")
