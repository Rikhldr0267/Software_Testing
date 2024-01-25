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

class TestGfg():
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
  
  def test_gfg(self):
    # Test name: gfg
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.geeksforgeeks.org/")
    # 2 | setWindowSize | 2064x1127 | 
    self.driver.set_window_size(2064, 1127)
    # 3 | mouseOver | linkText=DSA for Beginners | 
    element = self.driver.find_element(By.LINK_TEXT, "DSA for Beginners")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 4 | click | linkText=DSA for Beginners | 
    self.driver.find_element(By.LINK_TEXT, "DSA for Beginners").click()
    # 5 | mouseOver | linkText=Data Structures | 
    element = self.driver.find_element(By.LINK_TEXT, "Data Structures")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 6 | mouseOver | css=.active | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".active")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 7 | runScript | window.scrollTo(0,204.8000030517578) | 
    self.driver.execute_script("window.scrollTo(0,204.8000030517578)")
    # 8 | click | css=.single-chapter-hidden-div-0 > .gfg-nuj-single-track-div:nth-child(1) > .gfg-nuj-single-track-title | 
    self.driver.find_element(By.CSS_SELECTOR, ".single-chapter-hidden-div-0 > .gfg-nuj-single-track-div:nth-child(1) > .gfg-nuj-single-track-title").click()
    # 9 | runScript | window.scrollTo(0,208.8000030517578) | 
    self.driver.execute_script("window.scrollTo(0,208.8000030517578)")
    # 10 | click | linkText=DSA in C++ | 
    self.vars["window_handles"] = self.driver.window_handles
    # 11 | storeWindowHandle | root | 
    self.driver.find_element(By.LINK_TEXT, "DSA in C++").click()
    # 12 | selectWindow | handle=${win391} | 
    self.vars["win391"] = self.wait_for_window(2000)
    # 13 | close |  | 
    self.vars["root"] = self.driver.current_window_handle
    # 14 | selectWindow | handle=${root} | 
    self.driver.switch_to.window(self.vars["win391"])
    # 15 | click | linkText=Array | 
    self.driver.close()
    # 16 | click | css=.gfg-nuj-heading-menu-tab:nth-child(2) > .gfg-nuj-heading-menu-tab-title | 
    self.driver.switch_to.window(self.vars["root"])
    # 17 | click | css=.gfg-nuj-heading-menu-tab:nth-child(3) > .gfg-nuj-heading-menu-tab-title | 
    self.driver.find_element(By.LINK_TEXT, "Array").click()
    # 18 | click | linkText=Trending Now | 
    self.driver.find_element(By.CSS_SELECTOR, ".gfg-nuj-heading-menu-tab:nth-child(2) > .gfg-nuj-heading-menu-tab-title").click()
    # 19 | mouseOver | linkText=Trending Now | 
    self.driver.find_element(By.CSS_SELECTOR, ".gfg-nuj-heading-menu-tab:nth-child(3) > .gfg-nuj-heading-menu-tab-title").click()
    # 20 | mouseOut | linkText=Trending Now | 
    self.driver.find_element(By.LINK_TEXT, "Trending Now").click()
    # 21 | mouseOver | linkText=Foundational Courses | 
    element = self.driver.find_element(By.LINK_TEXT, "Trending Now")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 22 | click | css=.gcse-search__btn | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 23 | type | id=gcse-search-input | Linux
    element = self.driver.find_element(By.LINK_TEXT, "Foundational Courses")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 24 | sendKeys | id=gcse-search-input | ${KEY_ENTER}
    self.driver.find_element(By.CSS_SELECTOR, ".gcse-search__btn").click()
    # 25 | click | linkText=What is Linux Operating System - GeeksforGeeks | 
    self.driver.find_element(By.ID, "gcse-search-input").send_keys("Linux")
    # 26 | runScript | window.scrollTo(0,800) | 
    self.driver.find_element(By.ID, "gcse-search-input").send_keys(Keys.ENTER)
    # 27 | click | linkText=LINUX Full Form | 
    self.driver.find_element(By.LINK_TEXT, "What is Linux Operating System - GeeksforGeeks").click()
    # 28 | runScript | window.scrollTo(0,1074.4000244140625) | 
    self.driver.execute_script("window.scrollTo(0,800)")
    # 29 | runScript | window.scrollTo(0,805.5999755859375) | 
    self.driver.find_element(By.LINK_TEXT, "LINUX Full Form").click()
    # 30 | click | css=.article-pgnavi_next span:nth-child(1) | 
    self.driver.execute_script("window.scrollTo(0,1074.4000244140625)")
    # 31 | mouseOver | linkText=How To Change Your YouTube Channel Name | 
    self.driver.execute_script("window.scrollTo(0,805.5999755859375)")
    self.driver.find_element(By.CSS_SELECTOR, ".article-pgnavi_next span:nth-child(1)").click()
    element = self.driver.find_element(By.LINK_TEXT, "How To Change Your YouTube Channel Name")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
  