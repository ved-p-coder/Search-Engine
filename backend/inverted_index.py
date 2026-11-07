from collections import Counter


class InvertedIndex:
    """Stores terms and the documents in which they appear."""

    def __init__(self):
        # Maps each term to its document IDs and term frequencies.
        # Example: {"python": {1: 2, 2: 1}}
        self.postings: dict[str, dict[int, int]] = {}

        # Stores the number of tokens in each document.
        self.document_lengths: dict[int, int] = {}
