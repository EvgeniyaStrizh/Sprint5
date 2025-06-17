from selenium.webdriver.support import expected_conditions as EC

from data import *
from locators import Locators


class TestUserRegistrationWithWrongEmail:
    def test_user_registration_with_wrong_email(self, driver):
        driver, wait = driver

        driver.find_element(*Locators.LOGIN_AND_REGISTRATION_BUTTON_XPATH).click()
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON_XPATH).click()

        email_input = driver.find_element(*Locators.EMAIL_INPUT_NAME)
        email_input_wrapper = driver.find_element(*Locators.EMAIL_INPUT_WRAPPER_XPATH)

        password_input = driver.find_element(*Locators.PASSWORD_INPUT_NAME)
        password_input_wrapper = driver.find_element(*Locators.PASSWORD_INPUT_WRAPPER_XPATH)

        submit_password_input = driver.find_element(*Locators.SUBMIT_PASSWORD_INPUT_NAME)
        submit_password_input_wrapper = driver.find_element(*Locators.SUBMIT_PASSWORD_INPUT_WRAPPER_XPATH)

        email_input.send_keys(TEST_EMAIL_1)
        password_input.send_keys(TEST_PASSWORD_1)
        submit_password_input.send_keys(TEST_PASSWORD_1)

        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON_XPATH).click()

        wait.until(EC.visibility_of_element_located(Locators.ERROR_MESSAGE_CSS_SELECTOR))

        error_message = driver.find_element(*Locators.ERROR_MESSAGE_CSS_SELECTOR)

        assert error_message.is_displayed(), "Текст ошибки не отображается"
        assert email_input_wrapper.value_of_css_property(
            "border-color") == EXPECTED_ERROR_BORDER_COLOR, "Цвет бордера поля email не соответствует ожидаемому"
        assert password_input_wrapper.value_of_css_property(
            "border-color") == EXPECTED_ERROR_BORDER_COLOR, "Цвет бордера поля password не соответствует ожидаемому"
        assert submit_password_input_wrapper.value_of_css_property(
            "border-color") == EXPECTED_ERROR_BORDER_COLOR, "Цвет бордера поля submitPassword не соответствует ожидаемому"
