from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import AccountProfilePageLocators, MainPageLocators


class TestRedirectOnPersonalAccount:
    def test_redirect_on_personal_account_by_clicking_button_for_auth_users(self, driver, login):

        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()
        profile_but = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AccountProfilePageLocators.PROFILE_BUTTON))
        assert "Профиль" in profile_but.text
