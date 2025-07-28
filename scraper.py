import os
from selenium import webdriver
from bs4 import BeautifulSoup


def get_driver() -> webdriver.Remote:
    """
    Return a WebDriver instance that connects to the remote browser specified
    by the `BROWSER_URL` environment variable. Recommended options for Docker
    are used.
    """
    browser_url = os.environ.get("BROWSER_URL", "http://localhost:4444/wd/hub")
    options = webdriver.ChromeOptions()
    # Reduce shared memory usage inside containers
    options.add_argument("--disable-dev-shm-usage")
    # Do not add --headless so we can watch the browser via noVNC
    return webdriver.Remote(command_executor=browser_url, options=options)


def main():
    # Example page. Change it to the URL you want to scrape.
    url = "https://example.com"
    driver = get_driver()
    try:
        driver.get(url)
        # Extract the HTML after the page has fully loaded
        soup = BeautifulSoup(driver.page_source, "html.parser")
        print("Page title:", soup.title.get_text() if soup.title else "(untitled)")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()