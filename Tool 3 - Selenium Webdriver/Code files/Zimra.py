# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 19:21:53 2024

@author: RIK HALDER
"""

# -*- coding: utf-8 -*-


# Required Python Packages:
# - selenium
# - beautifulsoup4
#pip install selenium beautifulsoup4

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Function to initialize and configure the Edge webdriver
def configure_webdriver():
    options = webdriver.EdgeOptions()
    options.use_chromium = True
    # options.add_argument('--headless')  # Run Edge in headless mode
    return webdriver.Edge(options=options)

# Function to perform the login
def perform_login(driver, username, password):
    try:
        # Open the NIT Rourkela portal
        driver.get("https://mail.nitrkl.ac.in/#1")

        # Find the username and password input fields
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='username']"))
        )
        password_field = driver.find_element(By.XPATH, "//input[@id='password']")

        # password_field = driver.find_element_by_id("LoginUserPassword_auth_password")

        # Input the username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Wait for the login to complete
        WebDriverWait(driver, 10).until(
            EC.title_contains("Your Expected Title on Successful Login")
        )

        # Check if the login was successful using BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        if "Your Expected Text on Successful Login" in soup.get_text():
            print("Login successful!")
        else:
            print("Login failed!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
def main():
    # login_url = 'https://login.nitrkl.ac.in/PortalMain'
    username = '223cs####'
    password = '#########'

    driver = None  # Initialize the driver outside the try block

    while True:
        try:
            # Configure and initialize the Edge webdriver
            driver = configure_webdriver()

            # Perform the login
            perform_login(driver, username, password)

        finally:
            if driver is not None:
                # Close the webdriver if it is initialized
                driver.quit()

                # Display success message after a successful login
                print("Login successfully!")

            # Wait for 10 hours before the next login attempt
            print("Waiting for 10 hours before the next login attempt...")
            time.sleep(10 * 60 * 60)

if __name__ == "__main__":
    main()
