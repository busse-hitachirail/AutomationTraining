import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_letskodeit_practice_page(setup_browser):
    driver = setup_browser
    try:
        driver.get("https://www.letskodeit.com/practice")
        time.sleep(1)

        # 1. Enter text in the name field
        try:
            name_box = driver.find_element(By.ID, "name")
            name_box.send_keys("Naren")
            assert name_box.get_attribute("value") == "Naren"
            print("Step 1 Passed: Name entered")
        except Exception as e:
            print(f"Step 1 Failed: {e}")

        # 2. Select BMW radio button
        try:
            bmw_radio = driver.find_element(By.XPATH, "//input[@value='bmw']")
            bmw_radio.click()
            assert bmw_radio.is_selected()
            print("Step 2 Passed: BMW radio selected")
        except Exception as e:
            print(f"Step 2 Failed: {e}")

        # 3. Click Honda checkbox
        try:
            honda_checkbox = driver.find_element(By.CSS_SELECTOR, "#hondacheck")
            honda_checkbox.click()
            assert honda_checkbox.is_selected()
            print("Step 3 Passed: Honda checkbox selected")
        except Exception as e:
            print(f"Step 3 Failed: {e}")

        # 4. Select dropdown
        try:
            dropdown = driver.find_element(By.ID, "carselect")
            dropdown.click()
            print("Step 4 Passed: Dropdown clicked")
        except Exception as e:
            print(f"Step 4 Failed: {e}")

        # 5. Click alert button
        try:
            alert_button = driver.find_element(By.CSS_SELECTOR, "input#alertbtn")
            alert_button.click()
            time.sleep(2)
            driver.switch_to.alert.accept()
            print("Step 5 Passed: Alert handled")
        except Exception as e:
            print(f"Step 5 Failed: {e}")

    finally:
        time.sleep(2)
        print("Closing browser")
