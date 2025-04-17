import pytest
from utils.driver_factory import DriverFactory
from pages.login_page import LoginPage
import logging
import os

@pytest.fixture(scope="function")
def driver():
    """
    Pytest fixture to initialize and teardown WebDriver.
    """
    driver = DriverFactory.get_driver()
    yield driver
    DriverFactory.quit_driver()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to take screenshot on test failure and log the event.
    """
    outcome = yield
    result = outcome.get_result()
    if result.when == "call" and result.failed:
        driver = DriverFactory.get_driver()
        screenshot_path = os.path.join("screenshots", "failed_login.png")
        driver.save_screenshot(screenshot_path)
        logging.error(f"Test failed. Screenshot saved: {screenshot_path}")

def test_login(driver):
    """
    Main test function for logging into Washington Post.
    Uses dummy credentials.
    """
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.login("dummyemail@example.com", "fakePassword123")
