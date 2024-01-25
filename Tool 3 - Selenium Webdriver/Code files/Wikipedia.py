from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def perform_wikipedia_search(search_query):
    # Initialize the WebDriver
    browser = webdriver.Edge()

    # URL of the Wikipedia website
    url = "https://www.wikipedia.org/"

    # Open the Wikipedia website
    browser.get(url)

    # Locate the search input field
    wait = WebDriverWait(browser, 10)
    search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='search']")))

    # Input the search query
    search_input.send_keys(search_query)

    # Submit the form
    search_input.submit()

    # Wait for the search results page to load (adjust the time as needed)
    time.sleep(5)

    # Perform actions on the search results page or do whatever is needed
    # For example, printing the title of the current page
    print("Current Page Title:", browser.title)

    # Close the browser when done
    browser.quit()

# Example usage:
search_query = "Software testing"
perform_wikipedia_search(search_query)
