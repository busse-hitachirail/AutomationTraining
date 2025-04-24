from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.letskodeit.com/practice")
    yield driver
    sleep(2)
    driver.quit()

def test_enter_name(setup):
    name_box = WebDriverWait(setup, 10).until(
        EC.visibility_of_element_located((By.ID, "name"))
    )
    name_box.send_keys("Sasha")
    assert name_box.get_attribute("value") == "Sasha"



