from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://doodles.google/search/"
SEARCH_TERM = "Tech"


def main():
    """Search Google Doodles and print links from the results page."""
    driver = webdriver.Chrome()
    try:
        driver.get(URL)
        old_url = driver.current_url

        search = driver.find_element(By.NAME, "title_like")
        search.send_keys(SEARCH_TERM)
        search.send_keys(Keys.RETURN)

        WebDriverWait(driver, 20).until(EC.url_changes(old_url))
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[href]"))
        )

        for anchor in driver.find_elements(By.CSS_SELECTOR, "a[href]"):
            href = anchor.get_attribute("href")
            text = anchor.text.strip()
            if href:
                print(f"Available link: {href}")
                if text:
                    print(f"Link text: {text}")
                print()
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
