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

class TestFlipkart():
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
  
  def test_flipkart(self):
    # Test name: flipkart
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.flipkart.com/")
    # 2 | setWindowSize | 1936x1056 | 
    self.driver.set_window_size(1936, 1056)
    # 3 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 4 | mouseOver | linkText=Mobiles | 
    element = self.driver.find_element(By.LINK_TEXT, "Mobiles")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 5 | mouseOut | linkText=Mobiles | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 6 | click | name=q | 
    self.driver.find_element(By.NAME, "q").click()
    # 7 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 8 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 9 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 10 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 11 | type | name=q | algorithm book
    self.driver.find_element(By.NAME, "q").send_keys("algorithm book")
    # 12 | sendKeys | name=q | ${KEY_ENTER}
    self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    # 13 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 14 | click | css=.\_1AtVbE:nth-child(2) > .\_13oc-S > div:nth-child(2) .\_396cs4 | 
    self.vars["window_handles"] = self.driver.window_handles
    # 15 | storeWindowHandle | root | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1AtVbE:nth-child(2) > .\\_13oc-S > div:nth-child(2) .\\_396cs4").click()
    # 16 | selectWindow | handle=${win6670} | 
    self.vars["win6670"] = self.wait_for_window(2000)
    # 17 | runScript | window.scrollTo(0,0) | 
    self.vars["root"] = self.driver.current_window_handle
    # 18 | click | css=.\_3v1-ww | 
    self.driver.switch_to.window(self.vars["win6670"])
    # 19 | selectWindow | handle=${root} | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 20 | click | css=.\_167Mu3:nth-child(5) .\_4921Z:nth-child(2) .\_24_Dny | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_3v1-ww").click()
    # 21 | click | css=.\_167Mu3:nth-child(6) .\_4921Z:nth-child(1) .\_3879cV | 
    self.driver.switch_to.window(self.vars["root"])
    # 22 | runScript | window.scrollTo(0,0) | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_167Mu3:nth-child(5) .\\_4921Z:nth-child(2) .\\_24_Dny").click()
    # 23 | click | css=.\_1AtVbE:nth-child(2) div:nth-child(2) .\_396cs4 | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_167Mu3:nth-child(6) .\\_4921Z:nth-child(1) .\\_3879cV").click()
    # 24 | selectWindow | handle=${win3271} | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 25 | click | id=pincodeInputId | 
    self.vars["window_handles"] = self.driver.window_handles
    # 26 | type | id=pincodeInputId | 723101
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1AtVbE:nth-child(2) div:nth-child(2) .\\_396cs4").click()
    # 27 | click | css=.\_2P_LDn | 
    self.vars["win3271"] = self.wait_for_window(2000)
    # 28 | close |  | 
    self.driver.switch_to.window(self.vars["win3271"])
    # 29 | selectWindow | handle=${root} | 
    self.driver.find_element(By.ID, "pincodeInputId").click()
    # 30 | mouseOver | linkText=Grocery | 
    self.driver.find_element(By.ID, "pincodeInputId").send_keys("723101")
    # 31 | mouseOut | linkText=Grocery | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_2P_LDn").click()
    # 32 | mouseOver | css=.\_1AtVbE:nth-child(2) div:nth-child(4) .\_396cs4 | 
    self.driver.close()
    # 33 | mouseOut | css=.\_1AtVbE:nth-child(2) div:nth-child(4) .\_396cs4 | 
    self.driver.switch_to.window(self.vars["root"])
    element = self.driver.find_element(By.LINK_TEXT, "Grocery")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_1AtVbE:nth-child(2) div:nth-child(4) .\\_396cs4")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
  
