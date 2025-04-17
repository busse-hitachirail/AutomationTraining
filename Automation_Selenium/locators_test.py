from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElements():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elementsByID = driver.find_element(By.ID, "displayed-text")
        if elementsByID is not None:
            print("Element Found -> By Id")

        elementsByName = driver.find_element(By.NAME, "show-hide")
        if elementsByName is not None:
            print("Element Found -> By Name")

        elementsByXPath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        if elementsByXPath is not None:
            print("Element Found -> By XPath")

        elementsByCSS = driver.find_element(By.CSS_SELECTOR, "#displayed-text")
        if elementsByCSS is not None:
            print("Element Found -> By CSS")

run_tests = FindElements()
run_tests.test()