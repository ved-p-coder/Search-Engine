from pathlib import Path

from bs4 import BeautifulSoup

from backend.text_processing import extract_text


def load_html_document(file_path: Path) -> dict[str, str]:


    # Read the HTML file using UTF-8 so text is decoded consistently
    html = file_path.read_text(encoding="utf-8")

    # Parse the HTML so we can access its title and body separately
    soup = BeautifulSoup(html, "html.parser")

    # Extract the page title, using an empty string if it is missing
    title_tag = soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else ""

    #Extract readable text from the body, excluding scripts and styles
    content = soup.body if soup.body is not None else soup
    text = extract_text(str(content))

    # Return a simple record that other search-engine components can use
    return {
        "source": file_path.name,
        "title": title,
        "text": text,
    }
