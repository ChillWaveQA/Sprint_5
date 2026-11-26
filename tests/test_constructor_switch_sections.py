from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import MainPageLocators


class TestConstructionSectionsSwitch:
    def test_switch_to_construction_section_sauces(self, driver, login):
        driver.find_element(*MainPageLocators.SAUCE_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_attribute(MainPageLocators.SAUCE_BUTTON, 'class', 'tab_tab_type_current'))
        active_class = driver.find_element(*MainPageLocators.SAUCE_BUTTON).get_attribute('class')
        assert 'tab_tab_type_current' in active_class

    def test_switch_to_construction_section_fillings(self, driver, login):
        driver.find_element(*MainPageLocators.FILLINGS_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_attribute(MainPageLocators.FILLINGS_BUTTON, 'class', 'tab_tab_type_current'))
        active_class = driver.find_element(*MainPageLocators.FILLINGS_BUTTON).get_attribute('class')
        assert 'tab_tab_type_current' in active_class

    def test_switch_to_construction_section_buns(self, driver, login):
        driver.find_element(*MainPageLocators.SAUCE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_attribute(MainPageLocators.SAUCE_BUTTON, 'class', 'tab_tab_type_current'))

        driver.find_element(*MainPageLocators.BUNS_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_attribute(MainPageLocators.BUNS_BUTTON, 'class', 'tab_tab_type_current'))

        active_class = driver.find_element(*MainPageLocators.BUNS_BUTTON).get_attribute('class')
        assert 'tab_tab_type_current' in active_class
