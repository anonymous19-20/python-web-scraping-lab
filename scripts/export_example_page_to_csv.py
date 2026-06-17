import csv
from pathlib import Path

import requests
from bs4 import BeautifulSoup


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_FILE = PROJECT_ROOT / "data" / "example_page_export.csv"
URL = "https://example.com"


def main():
    """Export the title, first paragraph, and first link from example.com."""
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    row = [
        soup.h1.get_text(strip=True),
        soup.p.get_text(" ", strip=True),
        soup.a.get("href"),
    ]

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["title", "paragraph", "url"])
        writer.writerow(row)

    print(f"Saved data to {OUTPUT_FILE.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
