from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import conftest

driver = webdriver.Chrome()
driver.get(conftest.BASE_URL)

driver.find_element(By.XPATH, "//button[contains(text(), 'Разместить объявление')]").click()

pop_up = driver.find_element(By.CSS_SELECTOR, '.popUp_shell__LuyqR')

assert pop_up.is_displayed(), "Модальное окно не отображается"

print("Отображается модальное окно с заголовком 'Чтобы разместить объявление, авторизуйтесь'. Тест пройден успешно!")

driver.quit()