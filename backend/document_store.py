from pathlib import Path

# Import the functions and class we already created.
from backend.document_loader import load_html_document
from backend.inverted_index import InvertedIndex


class DocumentStore:
    def __init__(self):
        # Store each document's information using its ID.
        self.documents = {}

        # Create an inverted index for searching document text.
        self.index = InvertedIndex()

        # Keep track of the next document ID.
        self.next_document_id = 1
