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

    def load_directory(self, directory: Path):
        # Find all HTML files in the supplied directory.
        html_files = sorted(directory.glob("*.html"))

        # Load each HTML file into the document collection.
        for file_path in html_files:
            document = load_html_document(file_path)

            # Assign a unique ID to this document.
            document_id = self.next_document_id
            self.next_document_id += 1

            # Save the document's metadata and extracted text.
            self.documents[document_id] = document
            
            #Add the document's text to the inverted index
            self.index.add_document(document_id, document["text"])
