from selenium.webdriver.common.by import By

class Locators:
    # --- Авторизация ---
    LOGIN_AND_REGISTRATION_BUTTON_XPATH = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    NO_ACCOUNT_BUTTON_XPATH = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    EMAIL_INPUT_NAME = (By.NAME, "email")
    EMAIL_INPUT_WRAPPER_XPATH = (By.XPATH, "//input[@name='email']/parent::div")
    PASSWORD_INPUT_NAME = (By.NAME, "password")
    PASSWORD_INPUT_WRAPPER_XPATH = (By.XPATH, "//input[@name='password']/parent::div")
    SUBMIT_PASSWORD_INPUT_NAME = (By.NAME, "submitPassword")
    SUBMIT_PASSWORD_INPUT_WRAPPER_XPATH = (By.XPATH, "//input[@name='submitPassword']/parent::div")
    CREATE_ACCOUNT_BUTTON_XPATH = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    LOGIN_BUTTON_XPATH = (By.XPATH, "//button[contains(text(), 'Войти')]")
    LOGOUT_BUTTON_XPATH = (By.XPATH, "//button[contains(text(), 'Выйти')]")

    # --- Профиль пользователя ---
    AVATAR_BUTTON_XPATH = (By.XPATH, "//button[@class='circleSmall']")
    USER_NAME = (By.NAME, "name")

    # --- Ошибки / уведомления ---
    ERROR_MESSAGE_CSS_SELECTOR = (By.CSS_SELECTOR, ".input_span__yWPqB")
    POPUP_CSS_SELECTOR = (By.CSS_SELECTOR, ".popUp_shell__LuyqR")

    # --- Создание объявления ---
    CREATE_AD_BUTTON_XPATH = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    TITLE_INPUT_NAME = (By.NAME, "name")
    DESCRIPTION_INPUT_XPATH = (By.XPATH, "//textarea[@name='description']")
    PRICE_INPUT_NAME = (By.NAME, "price")
    POST_AD_BUTTON_XPATH = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")
    AD_RADIO_XPATH = (By.XPATH, "(//input[@name='condition']/following-sibling::div)[1]")

    # --- Элементы формы / выпадающие списки ---
    INPUT_ARROW_DOWN_BUTTON_CSS_SELECTOR = (By.CSS_SELECTOR, "button[class*='dropDownMenu_arrowDown']")
    DROPDOWN_ITEM_XPATH = (By.XPATH, "(//div[contains(@class, 'dropDownMenu_options')]//button)[2]")

    # --- Мои объявления ---
    MY_AD_TITLE_XPATH = (By.XPATH, "//*[starts-with(@class, 'profilePage_listningBlock')]//div[@class='about']//h2[@class='h2'][1]")
    MY_AD_CITY_XPATH = (By.XPATH, "//*[starts-with(@class, 'profilePage_listningBlock')]//div[@class='about']//h3[@class='h3'][1]")
    MY_AD_PRICE_XPATH = (By.XPATH, "//*[starts-with(@class, 'profilePage_listningBlock')]//div[@class='price']/h2[@class='h2']")