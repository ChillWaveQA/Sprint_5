from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import user_email, user_pass
from locators import (
    AuthorizationLocators,
    ForgotPasswordPageLocators,
    MainPageLocators,
    RegistrationLocators,
)
from url import FORGOT_PASSWORD_URL, MAIN_URL, REGISTRATION_URL


class TestSuccessAuthorization:

    def test_success_auth_by_click__enter_button_on_main_page(self, driver):
        driver.get(MAIN_URL)
        driver.find_element(*MainPageLocators.AUTH_ACC_BUTTON).click()
        driver.find_element(*AuthorizationLocators.AUTH_EMAIL_FIELD).send_keys(user_email)
        driver.find_element(*AuthorizationLocators.AUTH_PASSWORD_FIELD).send_keys(user_pass)
        driver.find_element(*AuthorizationLocators.AUTH_BUTTON).click()
        order_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        assert "Оформить заказ" in order_button.text

    def test_success_auth_by_click_account_button_on_main_page(self, driver):
        driver.get(MAIN_URL)
        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()
        driver.find_element(*AuthorizationLocators.AUTH_EMAIL_FIELD).send_keys(user_email)
        driver.find_element(*AuthorizationLocators.AUTH_PASSWORD_FIELD).send_keys(user_pass)
        driver.find_element(*AuthorizationLocators.AUTH_BUTTON).click()
        order_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        assert "Оформить заказ" in order_button.text

    def test_success_auth_by_click_enter_button_on_reg_page(self, driver):
        driver.get(REGISTRATION_URL)
        driver.find_element(*RegistrationLocators.REG_LOGIN_BUTTON).click()
        driver.find_element(*AuthorizationLocators.AUTH_EMAIL_FIELD).send_keys(user_email)
        driver.find_element(*AuthorizationLocators.AUTH_PASSWORD_FIELD).send_keys(user_pass)
        driver.find_element(*AuthorizationLocators.AUTH_BUTTON).click()
        order_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        assert "Оформить заказ" in order_button.text

    def test_success_auth_by_click_enter_button_on_forgot_pass_page(self, driver):
        driver.get(FORGOT_PASSWORD_URL)
        driver.find_element(*ForgotPasswordPageLocators.FORGOT_PASS_LOGIN_BUTTON).click()
        driver.find_element(*AuthorizationLocators.AUTH_EMAIL_FIELD).send_keys(user_email)
        driver.find_element(*AuthorizationLocators.AUTH_PASSWORD_FIELD).send_keys(user_pass)
        driver.find_element(*AuthorizationLocators.AUTH_BUTTON).click()
        order_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        assert "Оформить заказ" in order_button.text
