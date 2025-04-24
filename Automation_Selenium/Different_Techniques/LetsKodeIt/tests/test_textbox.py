import pytest
from pages.practice_page import PracticePage

@pytest.mark.textbox
def test_enter_name(driver):
    page = PracticePage(driver)
    page.enter_name("Naren")
