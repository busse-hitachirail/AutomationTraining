import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup WebDriver
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.letskodeit.com/practice")
    yield driver
    time.sleep(2)
    driver.quit()

# Helper function to skip if number is in the list
def skip_if_needed(test_number, skip_list):
    if str(test_number) in skip_list:
        pytest.skip(f"Test {test_number} skipped by user input")

# Test 1
def test_1_enter_name(driver, skip_list):
    skip_if_needed(1, skip_list)
    name_box = driver.find_element(By.ID, "name")
    name_box.send_keys("Naren")
    print("✅ Test 1 - Enter Name: PASSED")

# Test 2
def test_2_select_bmw(driver, skip_list):
    skip_if_needed(2, skip_list)
    bmw_radio = driver.find_element(By.XPATH, "//input[@value='bmw']")
    bmw_radio.click()
    print("✅ Test 2 - BMW Radio Button: PASSED")

# Test 3
def test_3_click_honda_checkbox(driver, skip_list):
    skip_if_needed(3, skip_list)
    checkbox = driver.find_element(By.CSS_SELECTOR, "#hondacheck")
    checkbox.click()
    print("✅ Test 3 - Honda Checkbox: PASSED")

# Test 4
def test_4_select_dropdown(driver, skip_list):
    skip_if_needed(4, skip_list)
    dropdown = driver.find_element(By.ID, "carselect")
    dropdown.click()
    print("✅ Test 4 - Dropdown: PASSED")

# Test 5
def test_5_alert(driver, skip_list):
    skip_if_needed(5, skip_list)
    alert_btn = driver.find_element(By.CSS_SELECTOR, "input#alertbtn")
    alert_btn.click()
    time.sleep(2)
    driver.switch_to.alert.accept()
    print("✅ Test 5 - Alert Accepted: PASSED")


    # Type this in you command line make sure your path is correct
    #  pytest -s test_skip_cl.py --skip=2,4 (I am skipping step 2 and 4)
