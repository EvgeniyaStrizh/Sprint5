from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import conftest

driver = webdriver.Chrome()
driver.get(conftest.BASE_URL)

driver.find_element(By.XPATH, "//button[contains(text(), 'Вход и регистрация')]").click()
driver.find_element(By.XPATH, "//button[contains(text(), 'Нет аккаунта')]").click()

email_input = driver.find_element(By.NAME, "email")
email_input_wrapper = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[5]/form/div[2]/div[1]/div/div")

password_input = driver.find_element(By.NAME, "password")
password_input_wrapper = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[5]/form/div[2]/div[2]/div/div")

submit_password_input = driver.find_element(By.NAME, "submitPassword")
submit_password_input_wrapper = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[5]/form/div[2]/div[3]/div/div")

email_input.send_keys("test@ru")
password_input.send_keys("12345")
submit_password_input.send_keys("12345")

driver.find_element(By.XPATH, "//button[contains(text(), 'Создать аккаунт')]").click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".input_span__yWPqB")))

error_message = driver.find_element(By.CSS_SELECTOR, '.input_span__yWPqB')
expected_error_border_color = "rgb(255, 105, 114)"

assert error_message.is_displayed(), "Текст ошибки не отображается"
assert email_input_wrapper.value_of_css_property("border-color") == expected_error_border_color, "Цвет бордера поля email не соответствует ожидаемому"
assert password_input_wrapper.value_of_css_property("border-color") == expected_error_border_color, "Цвет бордера поля password не соответствует ожидаемому"
assert submit_password_input_wrapper.value_of_css_property("border-color") == expected_error_border_color, "Цвет бордера поля submitPassword не соответствует ожидаемому"

print("Ошибка. Введен невалидный email. Тест пройден успешно!")

driver.quit()