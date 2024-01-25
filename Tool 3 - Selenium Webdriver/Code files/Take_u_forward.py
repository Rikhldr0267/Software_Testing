# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 19:27:25 2024

@author: RIK HALDER
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def perform_take_you_forward_search(search_query):
    # Initialize the WebDriver
    browser = webdriver.Edge()

    # URL of the Xbox website
    url = "https://takeuforward.org/"

    # Open the Xbox website
    browser.get(url)

    # Locate the search button and click on it
    wait = WebDriverWait(browser, 1)
    

    # Locate the search input field
    search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='wp-block-search__input-1']")))

    # Input the search query
    search_input.send_keys(search_query)

    # Press Enter to submit the search query (you can use search_input.submit() if needed)
    search_input.submit()

    # Wait for the search results page to load (adjust the time as needed)
    time.sleep(5)

    # Perform actions on the search results page or do whatever is needed
    # For example, printing the title of the current page
    print("Current Page Title:", browser.title)

    # Close the browser when done
    browser.quit()

# Example usage:
search_query = "DSA"
perform_take_you_forward_search(search_query)
