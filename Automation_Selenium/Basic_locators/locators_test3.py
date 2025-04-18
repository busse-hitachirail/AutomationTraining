from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.letskodeit.com/practice")

# Handle initial alert (Share the Practice Page)
try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print(f"Initial alert text: {alert.text}")
    alert.accept()
    print("Initial alert accepted - PASS")
except Exception as e:
    print(f"No initial alert appeared or already closed - SKIPPED: {e}")

# Test 1: Enter name into input box
try:
    name_input = driver.find_element(By.ID, "name")
    name_input.send_keys("Alan")
    print("Test 1 - Enter name - PASS")
except Exception as e:
    print(f"Test 1 - Enter name - FAIL: {e}")

# Test 2: Click BMW radio button
try:
    bmw_radio = driver.find_element(By.XPATH, "//input[@value='bmw']")
    bmw_radio.click()
    print("Test 2 - Click BMW radio - PASS")
except Exception as e:
    print(f"Test 2 - Click BMW radio - FAIL: {e}")

# Test 3: Click Honda checkbox
try:
    honda_checkbox = driver.find_element(By.CSS_SELECTOR, "#hondacheck")
    honda_checkbox.click()
    print("Test 3 - Click Honda checkbox - PASS")
except Exception as e:
    print(f"Test 3 - Click Honda checkbox - FAIL: {e}")

# Test 4: Select dropdown
try:
    dropdown = driver.find_element(By.ID, "carselect")
    dropdown.click()
    print("Test 4 - Open dropdown - PASS")
except Exception as e:
    print(f"Test 4 - Open dropdown - FAIL: {e}")

# Test 5: Click alert button and accept alert
try:
    alert_btn = driver.find_element(By.ID, "alertbtn")
    alert_btn.click()
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print(f"Alert text: {alert.text}")
    alert.accept()
    print("Test 5 - Alert button clicked and alert accepted - PASS")
except Exception as e:
    print(f"Test 5 - Alert button test - FAIL: {e}")

# Clean up
time.sleep(2)
driver.quit()
print("Browser closed.")
