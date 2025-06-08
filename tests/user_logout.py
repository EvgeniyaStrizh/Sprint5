from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import conftest

driver = webdriver.Chrome()
driver.get(conftest.BASE_URL)

driver.find_element(By.XPATH, "//button[contains(text(), 'Вход и регистрация')]").click()

driver.find_element(By.NAME, "email").send_keys("test@ya.ru")
driver.find_element(By.NAME, "password").send_keys("12345")
driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".circleSmall")))

driver.find_element(By.XPATH, "//button[contains(text(), 'Выйти')]").click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")))

try:
    user_name = driver.find_element(By.CLASS_NAME, "name")
    assert not user_name.is_displayed(), "Имя пользователя отображается"
except NoSuchElementException:
    print("Имя пользователя не отображается.") 

try:
    user_avatar = driver.find_element(By.CSS_SELECTOR, '.circleSmall')
    assert not user_avatar.is_displayed(), "Фото пользователя отображается"
except NoSuchElementException:
    print("Фото пользователя не отображается.") 

login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
assert login_button.is_displayed(), "Отображается кнопка 'Вход и регистрация'"

print('Пользователь разлогинен. Тест пройден успешно!')

driver.quit()