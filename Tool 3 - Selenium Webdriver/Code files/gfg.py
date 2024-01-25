# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 23:42:30 2024

@author: RIK HALDER
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

def perform_gfg_search(search_query):
    # Initialize the WebDriver
    browser = webdriver.Edge()

    # URL of the GeeksforGeeks website
    url = "https://www.geeksforgeeks.org/"

    # Open the GeeksforGeeks website
    browser.get(url)

    # Locate the search input field
    search_box = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[class='ant-input ant-input-lg']"))
    )

    # Input the search query
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    
    time.sleep(5)
    
   
# Example usage:
search_query = "Data Structures and algorithm"
perform_gfg_search(search_query)
