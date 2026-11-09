from collections import Counter


class InvertedIndex:
    """Stores terms and the documents in which they appear."""

    def __init__(self):
        # Maps each term to its document IDs and term frequencies.
        # Example: {"python": {1: 2, 2: 1}}
        self.postings: dict[str, dict[int, int]] = {}

        # Stores the number of tokens in each document.
        self.document_lengths: dict[int, int] = {}

    def add_document(self, document_id: int, text: str) -> None:
        #Add a document to the inverted index.

        # Remove an older version first to prevent stale postings.
        self.remove_document(document_id)

        # Convert the document into the same tokens used for queries.
        tokens = self._tokenize(text)

        # Count how many times each term appears in this document.
        term_frequencies = Counter(tokens)

        # Save the document's total token count.
        self.document_lengths[document_id] = len(tokens)

        # Add this document and its term frequencies to each posting list.
        for term, frequency in term_frequencies.items():
            if term not in self.postings:
                self.postings[term] = {}

            self.postings[term][document_id] = frequency
