from selenium.webdriver.support import expected_conditions as EC

from data import *
from locators import Locators


class TestUserLogout:
    def test_user_logout(self, driver):
        driver, wait = driver

        driver.find_element(*Locators.LOGIN_AND_REGISTRATION_BUTTON_XPATH).click()
        driver.find_element(*Locators.EMAIL_INPUT_NAME).send_keys(TEST_EMAIL_1)
        driver.find_element(*Locators.PASSWORD_INPUT_NAME).send_keys(TEST_PASSWORD_1)
        driver.find_element(*Locators.LOGIN_BUTTON_XPATH).click()

        wait.until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON_XPATH)).click()

        assert wait.until(
            EC.invisibility_of_element_located(Locators.USER_NAME)), "Имя пользователя всё ещё отображается"
        assert wait.until(EC.invisibility_of_element_located(
            Locators.AVATAR_BUTTON_XPATH)), "Аватар пользователя всё ещё отображается"

        login_button = wait.until(EC.visibility_of_element_located(Locators.LOGIN_AND_REGISTRATION_BUTTON_XPATH))
        assert login_button.is_displayed(), "Кнопка 'Вход и регистрация' не отображается"
