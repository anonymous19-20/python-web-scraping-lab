from pathlib import Path

from bs4 import BeautifulSoup


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_PAGE = PROJECT_ROOT / "samples" / "apache_default_page.html"


def main():
    """Print the first paragraph from the local Apache default page sample."""
    html = SAMPLE_PAGE.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "lxml")
    paragraph = soup.find("p")

    if paragraph is None:
        print("No paragraph text found.")
        return

    print(paragraph.get_text(" ", strip=True))


if __name__ == "__main__":
    main()
