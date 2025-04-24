import pytest # Fixture to Launch Webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# WebDriver fixture that initializes Chrome browser before each test and quits after
@pytest.fixture
def driver():
    # Setup Chrome using WebDriver Manager (no manual download)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.letskodeit.com/practice")  # Navigate to the Practice page
    yield driver  # This line gives the test access to the driver
    driver.quit()  # Teardown: closes browser after test finishes
