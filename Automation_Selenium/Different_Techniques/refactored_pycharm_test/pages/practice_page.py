import logging
from selenium.webdriver.common.by import By

class PracticePage:
    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, name):
        self.driver.find_element(By.ID, "name").send_keys(name)
        logging.info(f"Entered name: {name}")

    def select_bmw_radio(self):
        self.driver.find_element(By.XPATH, "//input[@value='bmw']").click()
        logging.info("Selected BMW radio button")

    def click_honda_checkbox(self):
        self.driver.find_element(By.CSS_SELECTOR, "#hondacheck").click()
        logging.info("Clicked Honda checkbox")

    def select_dropdown(self):
        self.driver.find_element(By.ID, "carselect").click()
        logging.info("Clicked dropdown menu")

    def click_alert_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "input#alertbtn").click()
        logging.info("Clicked alert button")
        self.driver.switch_to.alert.accept()
        logging.info("Alert accepted")
