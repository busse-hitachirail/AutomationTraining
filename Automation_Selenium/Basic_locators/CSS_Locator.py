from selenium import webdriver # Imports Selenium WebDriver Module
from selenium.webdriver.common.by import By # Allows locating of elements

# CSS Locators Use:
# ID Attribute: #idValue
# Class Attribute: .classValue
# Tag Name: tagname
# Attribute Value: tagname[attribute='value']


class FindByIdName():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)


        # CASE 1
        # Now Click on the BMW Radio Button - The ID is 'bmwradio'
        # You could also type #bmw or by input[id='bmwradio']
        elementByCSS = driver.find_element(By.CSS_SELECTOR, "input#bmwradio")
        if elementByCSS is not None:
            print("Element Found -> By CSS ID| ATTRIBUTE ")
        # Type this is Chrom Dev Tools Field: document.querySelector('#bmwradio') to verify

        # Case 2
       # < input id = "hide-textbox" class ="btn-style" value="Hide" type="button" >
       # So possible locators: <input id="hide-textbox" class="btn-style" value="Hide" type="button">
        elementByCSS = driver.find_element(By.CSS_SELECTOR, 'input#hide-textbox' )
        if elementByCSS is not None:
            print("Element Found -> By CSS ID| ATTRIBUTE ")

        # Case 3 - CheckBox
        elementByCSS = driver.find_element(By.CSS_SELECTOR, '#hondacheck')
        if elementByCSS is not None:
            print("Element Found -> By CSS ID| ATTRIBUTE ")

        # Case 4 - Dropdown
        # <select id="carselect" class="inputs">

        #elementByCSS = driver.find_element(By.CSS_SELECTOR, 'select.inputs')
        #if elementByCSS is not None:
            #print("Element Found -> By CSS ID| CASE 4 - 1 (Class) ")

        elementByCSS = driver.find_element(By.CSS_SELECTOR, '#carselect')
        if elementByCSS is not None:
            print("Element Found -> By CSS ID| CASE 4-2(By ID)") # Only Case that will work.

        #elementByCSS = driver.find_element(By.CSS_SELECTOR, 'select#carselect.inputs')
        #print("Element Found -> By CSS ID| CASE 4 - 3(By Select and Class ")


run_tests = FindByIdName()
run_tests.test()