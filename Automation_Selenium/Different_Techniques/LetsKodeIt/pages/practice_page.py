from selenium.webdriver.common.by import By

class PracticePage:
    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, name):
        self.driver.find_element(By.ID, "name").send_keys(name)

    def click_bmw_radio(self):
        self.driver.find_element(By.ID, "bmwradio").click()

    def click_honda_checkbox(self):
        self.driver.find_element(By.ID, "hondacheck").click()

    def select_dropdown(self):
        self.driver.find_element(By.ID, "carselect").click()

    def click_alert_button(self):
        self.driver.find_element(By.ID, "alertbtn").click()

    def accept_alert(self):
        self.driver.switch_to.alert.accept()
