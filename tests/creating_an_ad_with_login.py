from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import conftest
from consts import *

driver = webdriver.Chrome()
driver.get(conftest.BASE_URL)
wait = WebDriverWait(driver, 20)

driver.find_element(By.XPATH, LOGIN_AND_REGISTRATION_BUTTON_XPATH).click()

driver.find_element(By.NAME, EMAIL_INPUT_NAME).send_keys("test_3@yandex.ru")
driver.find_element(By.NAME, PASSWORD_INPUT_NAME).send_keys("dfgjnSfsg")
driver.find_element(By.XPATH, LOGIN_BUTTON_XPATH).click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, AVATAR_BUTTON_CSS_SELECTOR)))

driver.find_element(By.XPATH, CREATE_AD_BUTTON_XPATH).click()

expected_ad_title = "Красная шапочка"
expected_ad_description = "сказка"
expected_ad_city = "Санкт-Петербург"
expected_ad_price = "5000"

wait.until(EC.visibility_of_element_located((By.NAME, TITLE_INPUT_NAME))).send_keys(expected_ad_title)
driver.find_element(By.XPATH, DESCRIPTION_INPUT_XPATH).send_keys(expected_ad_description)
driver.find_element(By.NAME, PRICE_INPUT_NAME).send_keys(expected_ad_price)

driver.find_element(By.XPATH, CITY_INPUT_ARROW_DOWN_BUTTON_XPATH).click()
wait.until(EC.element_to_be_clickable((By.XPATH, CITY_DROPDOWN_ITEM_XPATH))).click()

driver.find_element(By.XPATH, CATEGORY_INPUT_ARROW_DOWN_BUTTON_XPATH).click()
wait.until(EC.element_to_be_clickable((By.XPATH, CATEGORY_DROPDOWN_ITEM_XPATH))).click()

driver.find_element(By.XPATH, AD_RADIO_XPATH).click()
driver.find_element(By.XPATH, POST_AD_BUTTON_XPATH).click()
wait.until(EC.element_to_be_clickable((By.XPATH, AVATAR_BUTTON_XPATH))).click()

ad_title = wait.until(EC.visibility_of_element_located((By.XPATH, MY_AD_TITLE_XPATH)))
ad_city = wait.until(EC.visibility_of_element_located((By.XPATH, MY_AD_CITY_XPATH)))
ad_price = wait.until(EC.visibility_of_element_located((By.XPATH, MY_AD_PRICE_XPATH)))

assert ad_title.text == expected_ad_title, "Название объявления не соответствует ожидаемому"
assert ad_city.text == expected_ad_city, "Город в объявлении не соответствует ожидаемому"
assert ad_price.text == f"{expected_ad_price} ₽", "Цена в объявлении не соответствует ожидаемому"

print("Объявление создано. Тест пройден успешно!")

driver.quit()