from selenium import webdriver
from selenium.webdriver.common.by import By # Allows locating of elements

class FindByIdName():

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        elementById = driver.find_element(By.ID,"name")

        if elementById is not None:
            print("We found an element by Id")

        elementByName = driver.find_element(By.NAME, "show-hide")

        if elementByName is not None:
            print("We found an element by Name")

        driver.get("https://www.yahoo.com/")
        # This one should fail because the Id is not static
        # Exception thrown: NoSuchElementException
        driver.find_element(By.ID, "yui_3_18_0_4_1463100170626_1148")

findS = FindByIdName()
findS.test()