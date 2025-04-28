import pytest
import yaml
from Browser_Multiple.driver_factory import DriverFactory
from Browser_Multiple.practice_page import PracticePage

# Read browsers from YAML
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)
browsers = config.get("browsers", ["chrome"])

@pytest.mark.parametrize("browser_name", browsers)
def test_practice_page(browser_name):
    driver = DriverFactory.get_driver(browser_name)
    practice_page = PracticePage(driver)

    try:
        practice_page.load()
        practice_page.enter_name("Naren")
        practice_page.click_alert_button()
        practice_page.accept_alert()
    finally:
        DriverFactory.quit_driver()
