from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import AuthorizationLocators, RegistrationLocators
from url import REGISTRATION_URL


class TestRegistrationSuccess:
    def test_registration_success(self, driver, random_email, random_pass):
        driver.get(REGISTRATION_URL)
        email = random_email
        password = random_pass

        driver.find_element(*RegistrationLocators.REG_NAME_FIELD).send_keys("Vitalii")
        driver.find_element(*RegistrationLocators.REG_EMAIL_FIELD).send_keys(email)
        driver.find_element(*RegistrationLocators.REG_PASSWORD_FIELD).send_keys(password)
        driver.find_element(*RegistrationLocators.REG_BUTTON).click()
        auth_form_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthorizationLocators.AUTH_FORM))
        assert "Вход" in auth_form_name.text

class TestRegistrationFailed:
    def test_registration_with_incorrect_pass(self, driver, random_email):
        driver.get(REGISTRATION_URL)
        email = random_email
        password = "1234"

        driver.find_element(*RegistrationLocators.REG_NAME_FIELD).send_keys("Vitalii")
        driver.find_element(*RegistrationLocators.REG_EMAIL_FIELD).send_keys(email)
        driver.find_element(*RegistrationLocators.REG_PASSWORD_FIELD).send_keys(password)
        driver.find_element(*RegistrationLocators.REG_BUTTON).click()

        assert "Некорректный пароль" in driver.find_element(*RegistrationLocators.PASSWORD_ERROR_MESSAGE).text
