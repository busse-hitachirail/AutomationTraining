from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.letskodeit.com/practice")

# Step 1: Wait for and handle the alert (the "Share the Practice Page" one)
try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Alert text:", alert.text)
    alert.accept()  # Clicks the OK button
    print("Alert accepted.")
except Exception as e:
    print("No alert appeared:", e)

# Step 2: Proceed with your test normally
driver.find_element(By.ID, "name").send_keys("Naren")
driver.find_element(By.XPATH, "//input[@value='bmw']").click()
driver.find_element(By.CSS_SELECTOR, "#hondacheck").click()
driver.find_element(By.ID, "carselect").click()
driver.find_element(By.ID, "alertbtn").click()

# Step 3: Handle alert from alert button
#WebDriverWait(driver, 5).until(EC.alert_is_present())
#driver.switch_to.alert.accept()

# Clean up
time.sleep(2)
driver.quit()
