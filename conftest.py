import random
import string

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import user_email, user_pass
from locators import AuthorizationLocators, MainPageLocators
from url import LOGIN_PAGE_URL


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()

    try:
        yield browser
    finally:
        browser.quit()

@pytest.fixture
def random_email():
    first_name = "Vitalii"
    last_name = "Antonichev"
    cohort_number = 59
    domain = "yandex.ru"
    random_digits = f"{random.randint(0, 999):03d}"
    email = f"{first_name.lower()}_{last_name.lower()}_{cohort_number}_{random_digits}@{domain}"
    return email

@pytest.fixture
def random_pass():
    length = random.randint(6, 10)
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@pytest.fixture
def login(driver):
    driver.get(LOGIN_PAGE_URL)
    driver.find_element(*AuthorizationLocators.AUTH_EMAIL_FIELD).send_keys(user_email)
    driver.find_element(*AuthorizationLocators.AUTH_PASSWORD_FIELD).send_keys(user_pass)
    driver.find_element(*AuthorizationLocators.AUTH_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
