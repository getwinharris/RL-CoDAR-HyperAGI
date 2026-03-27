"""
Dataset Loading for RLM
Load HF datasets directly to RLM context
"""

from datasets import load_dataset
from typing import Dict, List, Any, Generator


class DatasetStreamer:
    """Load HF datasets directly to RLM REPL as context variables"""

    def __init__(self, dataset_name: str = "fineweb", rlm_instance=None, limit: int = None):
        """
        Args:
            dataset_name: Name of dataset ("fineweb", "finewiki", "the-stack")
            rlm_instance: RLM instance to load context into
            limit: Maximum number of documents to stream
        """
        self.dataset_name = dataset_name
        self.rlm = rlm_instance
        self.limit = limit
        self.loaded_datasets = {}

    def stream_fineweb(self) -> Generator[Dict, None, None]:
        """
        Stream FineWeb dataset without downloading entire thing.

        Yields:
            Document dicts with 'text' and 'source' keys
        """
        print("Streaming FineWeb dataset...")
        ds = load_dataset(
            "HuggingFaceFW/fineweb",
            split="train",
            streaming=True,
        )
        count = 0
        for item in ds:
            if self.limit and count >= self.limit:
                break
            yield {
                "text": item.get("text", ""),
                "source": "fineweb",
            }
            count += 1
        print(f"✅ Streamed {count} FineWeb documents")

    def stream_finewiki(self) -> Generator[Dict, None, None]:
        """
        Stream FineWiki dataset.

        Yields:
            Document dicts with 'text', 'title', and 'source' keys
        """
        print("Streaming FineWiki dataset...")
        ds = load_dataset(
            "HuggingFaceFW/finewiki",
            split="train",
            streaming=True,
        )
        count = 0
        for item in ds:
            if self.limit and count >= self.limit:
                break
            yield {
                "text": item.get("text", ""),
                "title": item.get("title", ""),
                "source": "finewiki",
            }
            count += 1
        print(f"✅ Streamed {count} FineWiki documents")

    def stream_the_stack(self, language: str = "python") -> Generator[Dict, None, None]:
        """
        Stream The-Stack v2 code dataset.

        Args:
            language: Programming language filter

        Yields:
            Code file dicts with 'code', 'path', 'language', 'source' keys
        """
        print(f"Streaming The-Stack dataset (language={language})...")
        ds = load_dataset(
            "bigcode/the-stack-v2",
            data_dir=f"data/{language}",
            split="train",
            streaming=True,
        )
        count = 0
        for item in ds:
            if self.limit and count >= self.limit:
                break
            yield {
                "code": item.get("content", ""),
                "path": item.get("path", ""),
                "language": language,
                "source": "the-stack",
            }
            count += 1
        print(f"✅ Streamed {count} {language} files from The-Stack")

    def stream(self) -> Generator[Dict, None, None]:
        """Stream the configured dataset."""
        if self.dataset_name == "fineweb":
            yield from self.stream_fineweb()
        elif self.dataset_name == "finewiki":
            yield from self.stream_finewiki()
        elif self.dataset_name == "the-stack":
            yield from self.stream_the_stack()
        else:
            raise ValueError(f"Unknown dataset: {self.dataset_name}")

    def stream_to_repl(self, var_prefix: str = "context") -> Generator[str, None, None]:
        """
        Stream dataset as Python code to load into REPL.

        Args:
            var_prefix: Variable name prefix (e.g. "context" → context_0, context_1, ...)

        Yields:
            Python code strings that set context variables
        """
        for i, doc in enumerate(self.stream()):
            yield f"{var_prefix}_{i} = {repr(doc)}"

    def load_to_rlm_context(self, **kwargs):
        """
        Load dataset directly to RLM context.

        Args:
            **kwargs: Additional arguments for loading
        """
        if self.rlm is None:
            raise ValueError("RLM instance not provided")

        count = 0
        for i, doc in enumerate(self.stream()):
            self.rlm._persistent_env.load_context(doc)
            count += 1
            print(f"  Loaded context_{i}: {len(str(doc))} bytes")

        print(f"✅ Loaded {count} documents into RLM context")
        return count


class ByteGroupTokenizer:
    """
    Byte-group tokenizer for CoDAR.

    Groups contiguous bytes into tokens at natural boundaries.
    "Hello World!" → [[72,101,108,108,111], [32], [87,111,114,108,100,33]]
                      "Hello"                " "    "World!"

    Every byte is a real token — spaces, newlines, punctuation are all
    meaningful byte-group tokens needed for language formation.
    """

    # Boundary bytes — each becomes its own 1-byte token
    BOUNDARIES = {
        0x20,  # space
        0x0A,  # newline
        0x0D,  # carriage return
        0x09,  # tab
        0x00,  # null (padding)
    }

    def __init__(self):
        self.vocab_size = 256  # All possible byte values

    def tokenize(self, raw_bytes: list) -> list:
        """
        Group bytes at natural boundaries.

        Each boundary byte (space, newline, tab, null) becomes its own
        1-byte token. Contiguous non-boundary bytes form multi-byte tokens.

        Args:
            raw_bytes: List of integers (0-255)

        Returns:
            List of byte-group tokens (each a list of ints)
        """
        groups = []
        current_group = []

        for b in raw_bytes:
            if b in self.BOUNDARIES:
                if current_group:
                    groups.append(current_group)
                    current_group = []
                groups.append([b])  # boundary byte is its own token
            else:
                current_group.append(b)

        if current_group:
            groups.append(current_group)

        return groups

    def detokenize(self, groups: list) -> bytes:
        """
        Flatten byte-groups back to bytes.

        Args:
            groups: List of byte-group tokens

        Returns:
            Raw bytes
        """
        return bytes(b for group in groups for b in group)

    def encode(self, text: str) -> list:
        """
        Encode text to byte-group tokens.

        Args:
            text: Input text string

        Returns:
            List of byte-group tokens
        """
        return self.tokenize(list(text.encode('utf-8')))

    def decode(self, groups: list) -> str:
        """
        Decode byte-group tokens back to text.

        Args:
            groups: List of byte-group tokens

        Returns:
            Decoded text string
        """
        return self.detokenize(groups).decode('utf-8', errors='ignore')

    def get_stats(self, doc_stream: Generator) -> Dict:
        """
        Get byte distribution statistics from a document stream.

        Args:
            doc_stream: Generator of document dicts

        Returns:
            Statistics dictionary
        """
        byte_counts = [0] * 256
        total_bytes = 0
        total_docs = 0
        total_groups = 0

        for doc in doc_stream:
            text = doc.get("text", doc.get("code", ""))
            raw = list(text.encode('utf-8'))
            groups = self.tokenize(raw)

            total_bytes += len(raw)
            total_docs += 1
            total_groups += len(groups)

            for b in raw:
                byte_counts[b] += 1

        most_common = max(range(256), key=lambda i: byte_counts[i])
        least_common = min(range(256), key=lambda i: byte_counts[i])

        return {
            "total_bytes": total_bytes,
            "total_docs": total_docs,
            "total_groups": total_groups,
            "avg_bytes_per_doc": total_bytes / max(1, total_docs),
            "avg_groups_per_doc": total_groups / max(1, total_docs),
            "vocab_size": self.vocab_size,
            "most_common_byte": most_common,
            "most_common_count": byte_counts[most_common],
            "least_common_byte": least_common,
            "least_common_count": byte_counts[least_common],
        }


# Legacy alias for backward compatibility
ByteDatasetTokenizer = ByteGroupTokenizer


if __name__ == "__main__":
    # Test byte-group tokenizer
    tokenizer = ByteGroupTokenizer()

    text = "Hello World!"
    groups = tokenizer.encode(text)
    print(f"Text: {text!r}")
    print(f"Groups: {groups}")
    print(f"Decoded: {tokenizer.decode(groups)!r}")
    print(f"Token count: {len(groups)}")

    # Multi-line
    text2 = "Hello\nWorld\nFoo Bar"
    groups2 = tokenizer.encode(text2)
    print(f"\nText: {text2!r}")
    print(f"Groups: {groups2}")
    print(f"Token count: {len(groups2)}")
