from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import AccountProfilePageLocators, AuthorizationLocators, MainPageLocators


class TestLogoutFromPersonalAccount:
    def test_logout_from_personal_account(self, driver, login):
        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AccountProfilePageLocators.PROFILE_BUTTON))
        driver.find_element(*AccountProfilePageLocators.EXIT_BUTTON).click()
        auth_form_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthorizationLocators.AUTH_FORM))
        assert "Вход" in auth_form_name.text
