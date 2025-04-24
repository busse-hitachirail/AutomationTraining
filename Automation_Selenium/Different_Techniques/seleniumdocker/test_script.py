import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime

# -------------------------------
# Configure Logging
# -------------------------------
logging.basicConfig(
    level=logging.INFO,  # Logging level (INFO, ERROR, DEBUG, etc.)
    format="%(asctime)s [%(levelname)s] %(message)s"  # Log format
)

# -------------------------------
# Define Selenium Test Class
# -------------------------------
class SeleniumTest:
    def __init__(self, base_url="https://www.letskodeit.com/practice"):
        self.base_url = base_url  # Set the base URL for testing
        self.driver = self._init_driver()  # Initialize the Chrome WebDriver

    def _init_driver(self):
        """Configure and return headless Chromium WebDriver."""
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium"  # Path inside Docker
        chrome_options.add_argument("--headless=new")         # Use new headless mode
        chrome_options.add_argument("--disable-gpu")          # Disable GPU rendering
        chrome_options.add_argument("--no-sandbox")           # Required for Docker
        chrome_options.add_argument("--window-size=1920,1080")  # Emulate full HD screen

        logging.info("Initializing WebDriver...")
        return webdriver.Chrome(
            service=Service("/usr/bin/chromedriver"),
            options=chrome_options
        )

    def take_screenshot(self, name="screenshot"):
        """Capture a screenshot and save it with a timestamp."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Format: YYYYMMDD_HHMMSS
        filename = f"{name}_{timestamp}.png"
        filepath = os.path.join(os.getcwd(), filename)
        self.driver.save_screenshot(filepath)
        logging.info(f"Screenshot saved: {filepath}")  # Log screenshot path

    def run_alert_test(self):
        """Main test logic to handle JavaScript alert on the page."""
        try:
            logging.info(f"Navigating to {self.base_url}")
            self.driver.get(self.base_url)

            logging.info("Waiting for alert button to be visible...")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "alertbtn"))
            )

            # Find and click the alert button
            alert_button = self.driver.find_element(By.ID, "alertbtn")
            alert_button.click()

            logging.info("Waiting for alert to appear...")
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())

            # Handle alert
            alert = self.driver.switch_to.alert
            logging.info(f"Alert text: {alert.text}")
            alert.accept()
            logging.info("Alert accepted successfully.")

        except Exception as e:
            # On error, log the failure and take a screenshot
            logging.error(f"Test failed: {e}")
            self.take_screenshot("alert_failure")

        finally:
            # Ensure browser is closed no matter what
            self.driver.quit()
            logging.info("Browser closed.")

# -------------------------------
# Run test if this script is main
# -------------------------------
if __name__ == "__main__":
    test = SeleniumTest()         # Instantiate test class
    test.run_alert_test()         # Run the test
