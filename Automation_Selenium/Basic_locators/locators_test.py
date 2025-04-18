from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class FindElements():
    def test(self):
        baseURL = "http://www.google.com"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.maximize_window()
        time.sleep(2)  # Optional: Let the page load

        try:
            elementsByID = driver.find_element(By.ID, "displayed-text")
            print("✅ Element Found -> By ID")
        except NoSuchElementException:
            print("❌ Element NOT Found -> By ID")

        try:
            elementsByName = driver.find_element(By.NAME, "show-hide")
            print("✅ Element Found -> By Name")
        except NoSuchElementException:
            print("❌ Element NOT Found -> By Name")

        try:
            elementsByXPath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
            print("✅ Element Found -> By XPath")
        except NoSuchElementException:
            print("❌ Element NOT Found -> By XPath")

        try:
            elementsByCSS = driver.find_element(By.CSS_SELECTOR, "#displayed-text")
            print("✅ Element Found -> By CSS")
        except NoSuchElementException:
            print("Element NOT Found -> By CSS")

        driver.quit()


run_tests = FindElements()
run_tests.test()









