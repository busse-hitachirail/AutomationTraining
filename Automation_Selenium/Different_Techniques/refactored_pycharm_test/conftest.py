import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Load config once globally
with open("config.yaml") as f:
    config = yaml.safe_load(f)
BROWSER = config["pytest"].get("browser", "chrome").lower()

@pytest.fixture(scope="module")
def setup():
    driver = None
    try:
        if BROWSER == "chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif BROWSER == "firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif BROWSER == "edge":
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            raise ValueError(f"Unsupported browser: {BROWSER}")

        driver.maximize_window()
        driver.get("https://www.letskodeit.com/practice")
        yield driver

    except Exception as e:
        pytest.fail(f"Failed to start the WebDriver for {BROWSER}: {e}")

    finally:
        if driver:
            driver.quit()
