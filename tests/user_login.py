from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import conftest

driver = webdriver.Chrome()
driver.get(conftest.BASE_URL)

driver.find_element(By.XPATH, "//button[contains(text(), 'Вход и регистрация')]").click()

driver.find_element(By.NAME, "email").send_keys("test@ya.ru")
driver.find_element(By.NAME, "password").send_keys("12345")
driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".circleSmall")))

user_avatar = driver.find_element(By.CSS_SELECTOR, '.circleSmall')
user_name = driver.find_element(By.CLASS_NAME, "name")

assert user_name.text == "User.", "user_name не равен 'User.'"
assert user_avatar.is_displayed(), "user_avatar не отображается"

print("Пользователь залогинен. Тест пройден успешно!")

driver.quit()