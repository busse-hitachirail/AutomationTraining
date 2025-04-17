import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class DriverFactory:
    """
    Singleton class to create and manage a single WebDriver instance.
    Ensures that only one instance of the browser runs at a time.
    """

    _driver = None  # Class-level variable to hold WebDriver instance

    @staticmethod
    def get_driver():
        """
        Creates and returns the WebDriver instance.
        If already created, returns the existing one.
        """
        if DriverFactory._driver is None:
            try:
                # Chrome options to maximize the browser
                options = Options()
                options.add_argument("--start-maximized")

                # Replace this path with the actual path to your ChromeDriver
                service = Service("/usr/local/bin/chromedriver")
                DriverFactory._driver = webdriver.Chrome(service=service, options=options)
                logging.info("ChromeDriver started successfully.")
            except Exception as e:
                logging.error(f"Error initializing ChromeDriver: {e}")
                raise
        return DriverFactory._driver

    @staticmethod
    def quit_driver():
        """
        Quits the WebDriver session and resets the instance.
        """
        if DriverFactory._driver:
            DriverFactory._driver.quit()
            DriverFactory._driver = None
            logging.info("ChromeDriver session ended.")
