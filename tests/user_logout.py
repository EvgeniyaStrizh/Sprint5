from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from data import *


def test_user_logout(driver):
    driver, wait = driver

    driver.find_element(By.XPATH, LOGIN_AND_REGISTRATION_BUTTON_XPATH).click()
    driver.find_element(By.NAME, EMAIL_INPUT_NAME).send_keys(TEST_EMAIL_1)
    driver.find_element(By.NAME, PASSWORD_INPUT_NAME).send_keys(TEST_PASSWORD_1)
    driver.find_element(By.XPATH, LOGIN_BUTTON_XPATH).click()

    wait.until(EC.element_to_be_clickable((By.XPATH, LOGOUT_BUTTON_XPATH))).click()

    assert wait.until(
        EC.invisibility_of_element_located((By.CLASS_NAME, USER_NAME))), "Имя пользователя всё ещё отображается"
    assert wait.until(EC.invisibility_of_element_located(
        (By.XPATH, AVATAR_BUTTON_CSS_XPATH))), "Аватар пользователя всё ещё отображается"

    login_button = wait.until(EC.visibility_of_element_located((By.XPATH, LOGIN_AND_REGISTRATION_BUTTON_XPATH)))
    assert login_button.is_displayed(), "Кнопка 'Вход и регистрация' не отображается"
