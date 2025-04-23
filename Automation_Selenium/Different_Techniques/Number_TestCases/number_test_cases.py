import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.letskodeit.com/practice")
    yield driver
    time.sleep(2)
    driver.quit()

@pytest.mark.test_1
def test_1_enter_name(setup):
    try:
        name_box = setup.find_element(By.ID, "name")
        name_box.send_keys("Naren")
        print("✅ Test 1 - Enter Name: PASSED")
    except Exception as e:
        print(f"❌ Test 1 - Enter Name: FAILED - {e}")

@pytest.mark.test_2
def test_2_select_bmw_radio(setup):
    try:
        bmw_radio = setup.find_element(By.XPATH, "//input[@value='bmw']")
        bmw_radio.click()
        print("✅ Test 2 - Select BMW Radio: PASSED")
    except Exception as e:
        print(f"❌ Test 2 - Select BMW Radio: FAILED - {e}")

@pytest.mark.test_3
def test_3_click_honda_checkbox(setup):
    try:
        honda_checkbox = setup.find_element(By.CSS_SELECTOR, "#hondacheck")
        honda_checkbox.click()
        print("✅ Test 3 - Click Honda Checkbox: PASSED")
    except Exception as e:
        print(f"❌ Test 3 - Click Honda Checkbox: FAILED - {e}")

@pytest.mark.test_4
def test_4_select_dropdown(setup):
    try:
        dropdown = setup.find_element(By.ID, "carselect")
        dropdown.click()
        print("✅ Test 4 - Select Dropdown: PASSED")
    except Exception as e:
        print(f"❌ Test 4 - Select Dropdown: FAILED - {e}")

@pytest.mark.test_5
def test_5_click_alert_and_accept(setup):
    try:
        alert_button = setup.find_element(By.CSS_SELECTOR, "input#alertbtn")
        alert_button.click()
        time.sleep(2)
        setup.switch_to.alert.accept()
        print("✅ Test 5 - Alert Button and Accept: PASSED")
    except Exception as e:
        print(f"❌ Test 5 - Alert Button and Accept: FAILED - {e}")
