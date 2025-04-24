from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure headless options
chrome_options = Options()
chrome_options.binary_location = "/usr/bin/chromium"
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920,1080")

# Use system-installed chromedriver
driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=chrome_options)

# Go to page and trigger alert
driver.get("https://www.letskodeit.com/practice")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "alertbtn")))

alert_button = driver.find_element(By.ID, "alertbtn")
alert_button.click()

# Handle alert
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()

driver.quit()

