# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 01:17:13 2024

@author: RIK HALDER
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def perform_xbox_search(search_query):
    # Initialize the WebDriver
    browser = webdriver.Edge()

    # URL of the Xbox website
    url = "https://www.amazon.in/"

    # Open the Xbox website
    browser.get(url)

    # Locate the search button and click on it
    wait = WebDriverWait(browser, 1)
    

    # Locate the search input field
    search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#twotabsearchtextbox")))

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
search_query = "Software testing books"
perform_xbox_search(search_query)
