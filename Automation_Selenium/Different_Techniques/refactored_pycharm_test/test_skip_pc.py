import pytest
from pages.practice_page import PracticePage
from pages.driver_manager import DriverManager
import time

@pytest.fixture(scope="module")
def setup():
    driver = DriverManager.get_driver()
    yield driver
    DriverManager.quit_driver()

@pytest.mark.test_1
def test_enter_name(setup):
    PracticePage(setup).enter_name("Naren")

@pytest.mark.test_2
def test_select_bmw_radio(setup):
    PracticePage(setup).select_bmw_radio()

@pytest.mark.test_3
def test_click_honda_checkbox(setup):
    PracticePage(setup).click_honda_checkbox()

@pytest.mark.test_4
def test_select_dropdown(setup):
    PracticePage(setup).select_dropdown()

@pytest.mark.test_5
def test_alert_button(setup):
    time.sleep(2)
    PracticePage(setup).click_alert_button()
