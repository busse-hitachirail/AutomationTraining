from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PracticePage:
    def __init__(self, driver):
        self.driver = driver
        self.name_field = (By.ID, "name")
        self.alert_button = (By.ID, "alertbtn")

    def load(self):
        self.driver.get("https://www.letskodeit.com/practice")

    def enter_name(self, name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.name_field)
        ).send_keys(name)

    def click_alert_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.alert_button)
        ).click()

    def accept_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
