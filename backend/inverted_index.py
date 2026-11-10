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

    def remove_document(self, document_id: int) -> None:
        """Remove a document and its postings from the index."""

        # Remove the document's stored length, if it exists.
        self.document_lengths.pop(document_id, None)

        # Find and remove this document from every posting list.
        for term in list(self.postings):
            self.postings[term].pop(document_id, None)

            # Delete terms that no longer appear in any document.
            if not self.postings[term]:
                del self.postings[term]

    def get_postings(self, term: str) -> dict[int, int]:
        #Return the documents containing a term and their frequencies.

        # Normalize the search term using the shared text-processing pipeline.
        normalized_terms = self._tokenize(term)

        # This method expects one term at a time.
        if len(normalized_terms) != 1:
            return {}

        normalized_term = normalized_terms[0]

        # Return a copy so callers cannot accidentally change the index.
        return self.postings.get(normalized_term, {}).copy()

    def get_document_frequency(self, term: str) -> int:
        #Return the number of documents containing a term

        # Document frequency counts documents, not total occurrences.
        return len(self.get_postings(term))

