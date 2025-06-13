from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from data import *


def test_creating_an_ad_with_login(driver):
    driver, wait = driver

    driver.find_element(By.XPATH, LOGIN_AND_REGISTRATION_BUTTON_XPATH).click()

    driver.find_element(By.NAME, EMAIL_INPUT_NAME).send_keys(TEST_EMAIL_1)
    driver.find_element(By.NAME, PASSWORD_INPUT_NAME).send_keys(TEST_PASSWORD_1)
    driver.find_element(By.XPATH, LOGIN_BUTTON_XPATH).click()

    wait.until(EC.visibility_of_element_located((By.XPATH, AVATAR_BUTTON_CSS_XPATH)))

    driver.find_element(By.XPATH, CREATE_AD_BUTTON_XPATH).click()

    wait.until(EC.visibility_of_element_located((By.NAME, TITLE_INPUT_NAME))).send_keys(EXPECTED_AD_TITLE)
    driver.find_element(By.XPATH, DESCRIPTION_INPUT_XPATH).send_keys(EXPECTED_AD_DESCRIPTION)
    driver.find_element(By.NAME, PRICE_INPUT_NAME).send_keys(EXPECTED_AD_PRICE)

    driver.find_elements(By.CSS_SELECTOR, INPUT_ARROW_DOWN_BUTTON_CSS_SELECTOR)[0].click()
    wait.until(EC.element_to_be_clickable((By.XPATH, DROPDOWN_ITEM_XPATH))).click()

    driver.find_elements(By.CSS_SELECTOR, INPUT_ARROW_DOWN_BUTTON_CSS_SELECTOR)[1].click()
    wait.until(EC.element_to_be_clickable((By.XPATH, DROPDOWN_ITEM_XPATH))).click()

    driver.find_element(By.XPATH, AD_RADIO_XPATH).click()
    driver.find_element(By.XPATH, POST_AD_BUTTON_XPATH).click()

    wait.until(EC.presence_of_element_located((By.XPATH, AVATAR_BUTTON_CSS_XPATH))).click()

    ad_title = wait.until(EC.visibility_of_element_located((By.XPATH, MY_AD_TITLE_XPATH)))
    ad_city = wait.until(EC.visibility_of_element_located((By.XPATH, MY_AD_CITY_XPATH)))
    ad_price = wait.until(EC.visibility_of_element_located((By.XPATH, MY_AD_PRICE_XPATH)))

    assert ad_title.text == EXPECTED_AD_TITLE, "Название объявления не соответствует ожидаемому"
    assert ad_city.text == EXPECTED_AD_CITY, "Город в объявлении не соответствует ожидаемому"
    assert ad_price.text.replace(" ", "") == f"{EXPECTED_AD_PRICE}₽", "Цена в объявлении не соответствует ожидаемому"
