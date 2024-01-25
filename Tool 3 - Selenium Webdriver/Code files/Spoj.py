# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 19:46:53 2024

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
    url = "https://www.spoj.com/"

    # Open the W3Schools website
    browser.get(url)

    # Locate the search input field
    wait = WebDriverWait(browser, 1)


    # Locate the Problems button and click it
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//body/div[1]/div[1]/div[2]/div[2]/div[1]/nav[1]/ul[1]/li[1]/a[1]")))
    search_button.click()

    # Wait for the search results page to load (adjust the time as needed)
    time.sleep(5)



    

# Example usage:
search_query = "Web Development"
perform_W3cSchool_search(search_query)
