from selenium.webdriver.support import expected_conditions as EC

from data import *
from locators import Locators


class TestCreatingAnAdWithLogin:
    def test_creating_an_ad_with_login(self, driver):
        driver, wait = driver

        driver.find_element(*Locators.LOGIN_AND_REGISTRATION_BUTTON_XPATH).click()
        driver.find_element(*Locators.EMAIL_INPUT_NAME).send_keys(TEST_EMAIL_1)
        driver.find_element(*Locators.PASSWORD_INPUT_NAME).send_keys(TEST_PASSWORD_1)
        driver.find_element(*Locators.LOGIN_BUTTON_XPATH).click()

        wait.until(EC.visibility_of_element_located(Locators.AVATAR_BUTTON_XPATH))
        driver.find_element(*Locators.CREATE_AD_BUTTON_XPATH).click()
        wait.until(EC.visibility_of_element_located(Locators.TITLE_INPUT_NAME)).send_keys(EXPECTED_AD_TITLE)
        driver.find_element(*Locators.DESCRIPTION_INPUT_XPATH).send_keys(EXPECTED_AD_DESCRIPTION)
        driver.find_element(*Locators.PRICE_INPUT_NAME).send_keys(EXPECTED_AD_PRICE)
        driver.find_elements(*Locators.INPUT_ARROW_DOWN_BUTTON_CSS_SELECTOR)[0].click()
        wait.until(EC.element_to_be_clickable(Locators.DROPDOWN_ITEM_XPATH)).click()
        driver.find_elements(*Locators.INPUT_ARROW_DOWN_BUTTON_CSS_SELECTOR)[1].click()
        wait.until(EC.element_to_be_clickable(Locators.DROPDOWN_ITEM_XPATH)).click()
        driver.find_element(*Locators.AD_RADIO_XPATH).click()
        driver.find_element(*Locators.POST_AD_BUTTON_XPATH).click()
        wait.until(EC.presence_of_element_located(Locators.AVATAR_BUTTON_XPATH)).click()

        ad_title = wait.until(EC.visibility_of_element_located(Locators.MY_AD_TITLE_XPATH))
        ad_city = wait.until(EC.visibility_of_element_located(Locators.MY_AD_CITY_XPATH))
        ad_price = wait.until(EC.visibility_of_element_located(Locators.MY_AD_PRICE_XPATH))

        assert ad_title.text == EXPECTED_AD_TITLE, "Название объявления не соответствует ожидаемому"
        assert ad_city.text == EXPECTED_AD_CITY, "Город в объявлении не соответствует ожидаемому"
        assert ad_price.text.replace(" ", "") == f"{EXPECTED_AD_PRICE}₽", "Цена в объявлении не соответствует ожидаемому"
