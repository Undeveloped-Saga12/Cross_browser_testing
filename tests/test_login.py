import pytest
from pages.login_page import LoginPage
from utils.config import VALID_USERNAME,VALID_PASSWORD

@pytest.mark.parametrize("browser",["chrome","firefox","edge"],indirect=True)
def test_successful_login(browser):
    login_page=LoginPage(browser)
    login_page.open()
    login_page.login(VALID_USERNAME,VALID_PASSWORD)
    assert login_page.is_dashboard_displayed(),"login failed"