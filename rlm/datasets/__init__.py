"""
RLM Datasets Module
Stream datasets to REPL without downloading
"""

from rlm.datasets.stream_datasets import DatasetStreamer, ByteGroupTokenizer

# Legacy alias
ByteDatasetTokenizer = ByteGroupTokenizer

__all__ = [
    "DatasetStreamer",
    "ByteGroupTokenizer",
    "ByteDatasetTokenizer",
]
