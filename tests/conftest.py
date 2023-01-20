import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
    s = Service(r'C:\Users\sonya\PycharmProjects\Resources\chromedriver.exe')
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()
    yield driver
    driver.close()