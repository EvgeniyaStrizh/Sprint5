from selenium.webdriver.common.by import By

from data import *


def test_creating_an_ad_without_login(driver):
    driver, wait = driver

    driver.find_element(By.XPATH, CREATE_AD_BUTTON_XPATH).click()
    pop_up = driver.find_element(By.CSS_SELECTOR, POPUP_CSS_SELECTOR)

    assert pop_up.is_displayed(), "Модальное окно не отображается"
