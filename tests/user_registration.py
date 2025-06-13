from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import helpers
from data import *


def test_user_registration(driver):
    driver, wait = driver

    driver.find_element(By.XPATH, LOGIN_AND_REGISTRATION_BUTTON_XPATH).click()

    driver.find_element(By.XPATH, NO_ACCOUNT_BUTTON_XPATH).click()

    driver.find_element(By.NAME, EMAIL_INPUT_NAME).send_keys(helpers.generate_random_email())
    driver.find_element(By.NAME, PASSWORD_INPUT_NAME).send_keys(TEST_PASSWORD_1)
    driver.find_element(By.NAME, SUBMIT_PASSWORD_INPUT_NAME).send_keys(TEST_PASSWORD_1)
    driver.find_element(By.XPATH, CREATE_ACCOUNT_BUTTON_XPATH).click()

    wait.until(EC.visibility_of_element_located((By.XPATH, AVATAR_BUTTON_CSS_XPATH)))

    user_avatar = driver.find_element(By.XPATH, AVATAR_BUTTON_CSS_XPATH)
    user_name = driver.find_element(By.CLASS_NAME, USER_NAME)

    assert user_name.text == "User.", "user_name не равен 'User.'"
    assert user_avatar.is_displayed(), "user_avatar не отображается"
