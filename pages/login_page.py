from selenium.webdriver.common.by import By
from utils.config import BASE_URL

class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.url=BASE_URL

    Username_input=(By.ID,"user-name")
    Password_input=(By.ID,"password")
    login_button=(By.ID,"login-button")
    Dashboard_header=(By.CLASS_NAME,"app_logo")

    def open(self):
        self.driver.get(self.url)

    def login(self,username,password):
        self.driver.find_element(*self.Username_input).send_keys(username)
        self.driver.find_element(*self.Password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def is_dashboard_displayed(self):
        return self.driver.find_element(*self.Dashboard_header).is_displayed()


    