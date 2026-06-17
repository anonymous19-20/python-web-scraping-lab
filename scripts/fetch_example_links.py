import requests
from bs4 import BeautifulSoup


URL = "https://example.com"


def main():
    """Fetch example.com and print every link URL found on the page."""
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            print(href)


if __name__ == "__main__":
    main()
