from locators import Locators


class TestCreatingAnAdWithoutLogin:
    def test_creating_an_ad_without_login(self, driver):
        driver, wait = driver

        driver.find_element(*Locators.CREATE_AD_BUTTON_XPATH).click()
        pop_up = driver.find_element(*Locators.POPUP_CSS_SELECTOR)

        assert pop_up.is_displayed(), "Модальное окно не отображается"
