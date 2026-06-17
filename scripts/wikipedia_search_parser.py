from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


URL = "https://en.wikipedia.org/wiki/Main_Page"
SEARCH_TERM = "go"


def main():
    """Search Wikipedia with Selenium and print paragraph text from the results."""
    driver = webdriver.Chrome()
    try:
        driver.get(URL)

        search = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "search"))
        )
        search.click()
        search.send_keys(SEARCH_TERM)
        search.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(EC.url_contains("search"))
        soup = BeautifulSoup(driver.page_source, "lxml")
    finally:
        driver.quit()

    for paragraph in soup.find_all("p"):
        text = paragraph.get_text(" ", strip=True)
        if text:
            print(text)
            print()


if __name__ == "__main__":
    main()
