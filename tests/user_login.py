from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from data import *


def test_user_login(driver):
    driver, wait = driver

    driver.find_element(By.XPATH, LOGIN_AND_REGISTRATION_BUTTON_XPATH).click()

    driver.find_element(By.NAME, EMAIL_INPUT_NAME).send_keys(TEST_EMAIL_1)
    driver.find_element(By.NAME, PASSWORD_INPUT_NAME).send_keys(TEST_PASSWORD_1)
    driver.find_element(By.XPATH, LOGIN_BUTTON_XPATH).click()

    user_avatar = wait.until(EC.visibility_of_element_located((By.XPATH, AVATAR_BUTTON_CSS_XPATH)))
    user_name = driver.find_element(By.CLASS_NAME, USER_NAME)

    assert user_name.text == "User.", "user_name не равен 'User.'"
    assert user_avatar.is_displayed(), "user_avatar не отображается"
