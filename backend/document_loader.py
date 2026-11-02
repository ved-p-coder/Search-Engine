from pathlib import Path

from bs4 import BeautifulSoup

from backend.text_processing import extract_text


def load_html_document(file_path: Path) -> dict[str, str]:
    
