import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# WebDriver Setup Fixture
@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.letskodeit.com/practice")
    yield driver
    time.sleep(2)
    driver.quit()

# Skip logic function
def should_skip(test_number, skip_list):
    return str(test_number) in skip_list

# Test 1: Enter Name
@pytest.mark.test_1
def test_1_enter_name(setup, skip_list):
    print(f"Skip list:{skip_list}")
    if should_skip(1, skip_list):
        pytest.skip("Skipped by user input")
    try:
        name_box = setup.find_element(By.ID, "name")
        name_box.send_keys("Naren")
        print("✅ Test 1 - Enter Name: PASSED")
    except Exception as e:
        print(f"❌ Test 1 - Enter Name: FAILED - {e}")

# Test 2: Select BMW Radio Button
@pytest.mark.test_2
def test_2_select_bmw_radio(setup, skip_list):
    if should_skip(2, skip_list):
        pytest.skip("Skipped by user input")
    try:
        bmw_radio = setup.find_element(By.XPATH, "//input[@value='bmw']")
        bmw_radio.click()
        print("✅ Test 2 - Select BMW Radio: PASSED")
    except Exception as e:
        print(f"❌ Test 2 - Select BMW Radio: FAILED - {e}")

# Test 3: Click Honda Checkbox
@pytest.mark.test_3
def test_3_click_honda_checkbox(setup, skip_list):
    if should_skip(3, skip_list):
        pytest.skip("Skipped by user input")
    try:
        honda_checkbox = setup.find_element(By.CSS_SELECTOR, "#hondacheck")
        honda_checkbox.click()
        print("✅ Test 3 - Click Honda Checkbox: PASSED")
    except Exception as e:
        print(f"❌ Test 3 - Click Honda Checkbox: FAILED - {e}")



# Test 4: Select from Dropdown
@pytest.mark.test_4
def test_4_select_dropdown(setup, skip_list):
    if should_skip(4, skip_list):
        pytest.skip("Skipped by user input")
    try:
        dropdown = setup.find_element(By.ID, "carselect")
        dropdown.click()
        print("✅ Test 4 - Select Dropdown: PASSED")
    except Exception as e:
        print(f"❌ Test 4 - Select Dropdown: FAILED - {e}")

# Test 5: Click Alert Button and Accept
@pytest.mark.test_5
def test_5_click_alert_and_accept(setup, skip_list):
    if should_skip(5, skip_list):
        pytest.skip("Skipped by user input")
    try:
        alert_button = setup.find_element(By.CSS_SELECTOR, "input#alertbtn")
        alert_button.click()
        time.sleep(2)
        setup.switch_to.alert.accept()
        print("✅ Test 5 - Alert Button and Accept: PASSED")
    except Exception as e:
        print(f"❌ Test 5 - Alert Button and Accept: FAILED - {e}")
