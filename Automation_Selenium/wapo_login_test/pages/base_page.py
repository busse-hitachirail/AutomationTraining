import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    Base class to abstract common Selenium operations like click, input, wait.
    All page objects should inherit from this class.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Set explicit wait timeout

    def click(self, by_locator):
        """
        Click on the element located by 'by_locator' once it is clickable.
        """
        try:
            self.wait.until(EC.element_to_be_clickable(by_locator)).click()
            logging.info(f"Clicked on element: {by_locator}")
        except Exception as e:
            logging.error(f"Click failed on {by_locator}: {e}")
            raise

    def enter_text(self, by_locator, text):
        """
        Enters text into the input field located by 'by_locator'.
        """
        try:
            field = self.wait.until(EC.visibility_of_element_located(by_locator))
            field.clear()
            field.send_keys(text)
            logging.info(f"Entered text into element: {by_locator}")
        except Exception as e:
            logging.error(f"Text input failed on {by_locator}: {e}")
            raise

    def get_element(self, by_locator):
        """
        Returns a WebElement after waiting for it to be present in the DOM.
        """
        try:
            return self.wait.until(EC.presence_of_element_located(by_locator))
        except Exception as e:
            logging.error(f"Element not found: {by_locator}: {e}")
            raise
