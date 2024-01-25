# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestW3c():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_w3c(self):
    # Test name: w3c
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.w3schools.com/")
    # 2 | setWindowSize | 1502x815 | 
    self.driver.set_window_size(1502, 815)
    # 3 | mouseOver | linkText=DJANGO | 
    element = self.driver.find_element(By.LINK_TEXT, "DJANGO")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 4 | mouseOver | linkText=NODEJS | 
    element = self.driver.find_element(By.LINK_TEXT, "NODEJS")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 5 | mouseOut | linkText=NODEJS | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 6 | mouseOver | linkText=PYTHON | 
    element = self.driver.find_element(By.LINK_TEXT, "PYTHON")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 7 | click | linkText=PYTHON | 
    self.driver.find_element(By.LINK_TEXT, "PYTHON").click()
    # 8 | mouseOver | linkText=Python Get Started | 
    element = self.driver.find_element(By.LINK_TEXT, "Python Get Started")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 9 | click | linkText=Python Get Started | 
    self.driver.find_element(By.LINK_TEXT, "Python Get Started").click()
    # 10 | mouseOut | linkText=Python Get Started | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 11 | click | linkText=Python Booleans | 
    self.driver.find_element(By.LINK_TEXT, "Python Booleans").click()
    # 12 | mouseOver | linkText=Python Sets | 
    element = self.driver.find_element(By.LINK_TEXT, "Python Sets")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 13 | mouseOut | linkText=Python Sets | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 14 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 15 | click | linkText=Python Lambda | 
    self.driver.find_element(By.LINK_TEXT, "Python Lambda").click()
    # 16 | click | linkText=Try it Yourself » | 
    self.vars["window_handles"] = self.driver.window_handles
    # 17 | mouseOver | linkText=Try it Yourself » | 
    self.driver.find_element(By.LINK_TEXT, "Try it Yourself »").click()
    # 18 | storeWindowHandle | root | 
    self.vars["win7606"] = self.wait_for_window(2000)
    # 19 | selectWindow | handle=${win7606} | 
    element = self.driver.find_element(By.LINK_TEXT, "Try it Yourself »")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 20 | click | id=runbtn | 
    self.vars["root"] = self.driver.current_window_handle
    # 21 | close |  | 
    self.driver.switch_to.window(self.vars["win7606"])
    # 22 | selectWindow | handle=${root} | 
    self.driver.find_element(By.ID, "runbtn").click()
    # 23 | click | linkText=PHP | 
    self.driver.close()
    # 24 | click | linkText=JAVA | 
    self.driver.switch_to.window(self.vars["root"])
    # 25 | click | linkText=Java Variables | 
    self.driver.find_element(By.LINK_TEXT, "PHP").click()
    self.driver.find_element(By.LINK_TEXT, "JAVA").click()
    self.driver.find_element(By.LINK_TEXT, "Java Variables").click()
  