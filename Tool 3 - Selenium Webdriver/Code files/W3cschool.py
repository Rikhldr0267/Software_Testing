# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 19:39:19 2024

@author: RIK HALDER
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def perform_W3cSchool_search(search_query):
    # Initialize the WebDriver
    browser = webdriver.Edge()

    # URL of the W3Schools website
    url = "https://www.w3schools.com/"

    # Open the W3Schools website
    browser.get(url)

    # Locate the search input field
    wait = WebDriverWait(browser, 1)
    search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='search2']")))

    # Input the search query
    search_input.send_keys(search_query)

    # Locate the search button and click it
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='learntocode_searchbtn']")))
    search_button.click()

    # Wait for the search results page to load (adjust the time as needed)
    time.sleep(5)



    

# Example usage:
search_query = "Web Development"
perform_W3cSchool_search(search_query)
