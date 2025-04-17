from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging

class LoginPage(BasePage):
    """
    Page Object for the Washington Post login functionality.
    Uses locators and base page methods.
    """

    # Locators for the login flow
    SIGN_IN_BTN = (By.XPATH, "//a[@data-qa='nav-sign-in']")
    EMAIL_FIELD = (By.ID, "email")
    CONTINUE_BTN = (By.ID, "login-btn")
    PASSWORD_FIELD = (By.ID, "password")
    FINAL_LOGIN_BTN = (By.ID, "login-btn")  # Same ID reused

    def go_to_login_page(self):
        """
        Opens the Washington Post homepage.
        """
        try:
            self.driver.get("https://www.washingtonpost.com")
            logging.info("Navigated to Washington Post homepage.")
        except Exception as e:
            logging.error(f"Failed to open homepage: {e}")
            raise

    def login(self, email, password):
        """
        Performs the full login process with given email and password.
        """
        try:
            self.click(self.SIGN_IN_BTN)
            self.enter_text(self.EMAIL_FIELD, email)
            self.click(self.CONTINUE_BTN)
            self.enter_text(self.PASSWORD_FIELD, password)
            self.click(self.FINAL_LOGIN_BTN)
            logging.info("Login form submitted.")
        except Exception as e:
            logging.error(f"Login failed: {e}")
            raise
