from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.letskodeit.com/practice")

# 1. Enter text in the name field (using ID)
name_box = driver.find_element(By.ID, "name")
name_box.send_keys("Naren")

# 2. Select BMW radio button (using XPath)
bmw_radio = driver.find_element(By.XPATH, "//input[@value='bmw']")
bmw_radio.click()

# 3. Click Honda checkbox (using CSS Selector)
honda_checkbox = driver.find_element(By.CSS_SELECTOR, "#hondacheck")
honda_checkbox.click()

# 4. Select dropdown (using ID)
dropdown = driver.find_element(By.ID, "carselect")
dropdown.click()

# 5. Click alert button (using CSS Selector)
alert_button = driver.find_element(By.CSS_SELECTOR, "input#alertbtn")
alert_button.click()

# Handle alert
time.sleep(2)
driver.switch_to.alert.accept()

# Close browser
time.sleep(2)
driver.quit()
