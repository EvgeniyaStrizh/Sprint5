from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from data import *


def test_user_registration_with_wrong_email(driver):
    driver, wait = driver

    driver.find_element(By.XPATH, LOGIN_AND_REGISTRATION_BUTTON_XPATH).click()
    driver.find_element(By.XPATH, NO_ACCOUNT_BUTTON_XPATH).click()

    email_input = driver.find_element(By.NAME, EMAIL_INPUT_NAME)
    email_input_wrapper = driver.find_element(By.XPATH, EMAIL_INPUT_WRAPPER_XPATH)

    password_input = driver.find_element(By.NAME, PASSWORD_INPUT_NAME)
    password_input_wrapper = driver.find_element(By.XPATH, PASSWORD_INPUT_WRAPPER_XPATH)

    submit_password_input = driver.find_element(By.NAME, SUBMIT_PASSWORD_INPUT_NAME)
    submit_password_input_wrapper = driver.find_element(By.XPATH, SUBMIT_PASSWORD_INPUT_WRAPPER_XPATH)

    email_input.send_keys(TEST_EMAIL_1)
    password_input.send_keys(TEST_PASSWORD_1)
    submit_password_input.send_keys(TEST_PASSWORD_1)

    driver.find_element(By.XPATH, CREATE_ACCOUNT_BUTTON_XPATH).click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, INPUT_SPAN_CSS_SELECTOR)))

    error_message = driver.find_element(By.CSS_SELECTOR, INPUT_SPAN_CSS_SELECTOR)

    assert error_message.is_displayed(), "Текст ошибки не отображается"
    assert email_input_wrapper.value_of_css_property(
        "border-color") == EXPECTED_ERROR_BORDER_COLOR, "Цвет бордера поля email не соответствует ожидаемому"
    assert password_input_wrapper.value_of_css_property(
        "border-color") == EXPECTED_ERROR_BORDER_COLOR, "Цвет бордера поля password не соответствует ожидаемому"
    assert submit_password_input_wrapper.value_of_css_property(
        "border-color") == EXPECTED_ERROR_BORDER_COLOR, "Цвет бордера поля submitPassword не соответствует ожидаемому"
