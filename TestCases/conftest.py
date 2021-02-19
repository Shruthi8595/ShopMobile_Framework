
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    return parser.addoption("--browser")

@pytest.fixture(scope="class")
def setup(request):

    browser = request.config.getoption("--browser")
    if browser == "Ie":
        driver = webdriver.Ie()
    elif browser == "Chrome":
        driver = webdriver.Chrome()
    else :
        driver = webdriver.Firefox()

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()