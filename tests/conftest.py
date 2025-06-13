import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import data


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(data.BASE_URL)
    wait = WebDriverWait(driver, 20)
    yield driver, wait
    driver.quit()
