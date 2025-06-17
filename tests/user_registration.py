from selenium.webdriver.support import expected_conditions as EC

import helpers
from data import *
from locators import Locators


class TestUserRegistration:
    def test_user_registration(self, driver):
        driver, wait = driver

        driver.find_element(*Locators.LOGIN_AND_REGISTRATION_BUTTON_XPATH).click()

        driver.find_element(*Locators.NO_ACCOUNT_BUTTON_XPATH).click()

        driver.find_element(*Locators.EMAIL_INPUT_NAME).send_keys(helpers.generate_random_email())
        driver.find_element(*Locators.PASSWORD_INPUT_NAME).send_keys(TEST_PASSWORD_1)
        driver.find_element(*Locators.SUBMIT_PASSWORD_INPUT_NAME).send_keys(TEST_PASSWORD_1)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON_XPATH).click()

        wait.until(EC.visibility_of_element_located(Locators.AVATAR_BUTTON_XPATH))

        user_avatar = driver.find_element(*Locators.AVATAR_BUTTON_XPATH)
        user_name = driver.find_element(*Locators.USER_NAME)

        assert user_name.text == "User.", "user_name не равен 'User.'"
        assert user_avatar.is_displayed(), "user_avatar не отображается"
