import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

def pytest_addoption(parser):
    parser.addoption(
        "--browser",action="store",default="chrome",help="Brower to run tests:chrome,firefox,edge"
    )
    # parser.addoption("--cloud",action="store",default="browserstack",help="browser or cloud")

@pytest.fixture(scope="function")
def browser(request):
    cloud_provider=request.config.getoption("--cloud")
    browser_name=request.config.getoption("--browser").lower()
    driver=None

    if browser_name =="chrome":
        service=ChromeService(executable_path=r"C:\Automation Tools\chromedriver.exe")
        options=webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        driver=webdriver.Chrome(service=service,options=options)
    elif browser_name =="firefox":
        service=FirefoxService(executable_path=r"C:\Automation Tools\geckodriver.exe")
        options=webdriver.FirefoxOptions()
        options.add_argument("--headless")
        driver=webdriver.Firefox(service=service,options=options)
    elif browser_name =="edge":
        service=EdgeService(executable_path=r"C:\Automation Tools\msedgedriver.exe")
        options=webdriver.EdgeOptions()
        options.add_argument("--headless")
        driver=webdriver.Edge(service=service,options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    driver.implicitly_wait(10)
    yield driver
    driver.quit()