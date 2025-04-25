import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import yaml

# Configure logging
logging.basicConfig(
    filename='test_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DriverManager:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            logging.info("Initializing WebDriver...")
            with open("config.yaml") as f:
                config = yaml.safe_load(f)
            browser = config["pytest"].get("browser", "chrome").lower()

            try:
                if browser == "chrome":
                    cls._driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
                elif browser == "firefox":
                    cls._driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
                elif browser == "edge":
                    cls._driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
                else:
                    raise ValueError(f"Unsupported browser: {browser}")

                cls._driver.maximize_window()
                cls._driver.get("https://www.letskodeit.com/practice")
                logging.info(f"{browser.capitalize()} browser launched successfully.")
            except Exception as e:
                logging.error(f"Error initializing WebDriver for {browser}: {e}")
                raise

        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            logging.info("WebDriver session closed.")
            cls._driver = None
