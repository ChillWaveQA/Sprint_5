from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import AccountProfilePageLocators, MainPageLocators


class TestConstructorEntering:
    def test_constructor_enter_by_click_on_constuctor_button_from_pers_acc(self, driver, login):
        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AccountProfilePageLocators.PROFILE_BUTTON))
        driver.find_element(*AccountProfilePageLocators.CONSTRUCTOR_BUTTON).click()
        constructor_name = WebDriverWait(driver,10).until(EC.visibility_of_element_located(MainPageLocators.CONSTRUCT_BURGER))
        assert "Соберите бургер" in constructor_name.text

    def test_constructor_enter_by_click_on_logo_from_pers_acc(self, driver, login):
        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AccountProfilePageLocators.PROFILE_BUTTON))
        driver.find_element(*AccountProfilePageLocators.LOGO_SVG).click()
        constructor_name = WebDriverWait(driver,10).until(EC.visibility_of_element_located(MainPageLocators.CONSTRUCT_BURGER))
        assert "Соберите бургер" in constructor_name.text
