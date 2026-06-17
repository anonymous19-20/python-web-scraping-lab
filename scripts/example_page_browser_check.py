import requests
from bs4 import BeautifulSoup
from selenium import webdriver


URL = "https://example.com"


def main():
    """Compare the Example Domain heading from Requests with the browser title."""
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    print(f"Heading from Requests: {soup.h1.get_text(strip=True)}")

    driver = webdriver.Chrome()
    try:
        driver.get(URL)
        print(f"Browser title from Selenium: {driver.title}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
