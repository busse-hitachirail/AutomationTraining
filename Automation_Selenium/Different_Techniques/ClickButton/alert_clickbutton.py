from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Navigate to the Practice Page
driver.get("https://www.letskodeit.com/practice")

# Wait until the page is fully loaded
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "alertbtn")))


# Click the "Alert" button
alert_button = driver.find_element(By.ID, "alertbtn")
alert_button.click()

# Wait for the alert to be present
WebDriverWait(driver, 10).until(EC.alert_is_present())

# Switch to the alert and accept it
alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()

# Close the browser
driver.quit()

