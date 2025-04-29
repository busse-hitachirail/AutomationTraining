import allure
from sampletest_demo.base_page import BasePage
from sampletest_demo.practice_page_locators import PracticePageLocators

class PracticePage(BasePage):

    @allure.step('Click BMW Radio Button')
    def click_radio_button(self):
        self.click_element(PracticePageLocators.RADIO_BUTTON)

    @allure.step('Select BMW Checkbox')
    def select_checkbox_one(self):
        self.click_element(PracticePageLocators.CHECKBOX_ONE)

    @allure.step('Select Dropdown')
    def select_dropdown(self):
        self.click_element(PracticePageLocators.DROPDOWN)

    @allure.step('Enter Name into TextBox')
    def enter_name(self, name):
        self.enter_text(PracticePageLocators.TEXT_BOX, name)

    @allure.step('Switch to New Tab')
    def click_switch_tab(self):
        self.click_element(PracticePageLocators.SWITCH_TAB)

    @allure.step('Read Radio Button Header Text')
    def read_relative_xpath_element_one(self):
        return self.get_text(PracticePageLocators.RELATIVE_XPATH_ONE)
