from pathlib import Path

from bs4 import BeautifulSoup


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_PAGE = PROJECT_ROOT / "samples" / "example_domain.html"


def main():
    """Print the first link from the local Example Domain sample page."""
    html = SAMPLE_PAGE.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "lxml")
    first_link = soup.find("a")

    if first_link is None:
        print("No links found.")
        return

    print(first_link.get("href"))


if __name__ == "__main__":
    main()
