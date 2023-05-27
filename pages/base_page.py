import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator),
                                                    message=f"Couldn't find element by locator: {locator}")

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_all_elements_located(locator))

    def wait_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_any_elements_located(locator))

    def send_key(self, locator, key):
        return self.find_element(locator).send_keys(key)

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def mouse_click(self, locator):
        self.find_element(locator).click()

    @allure.step("Принимаем куки")
    def accept_cookies(self):
        self.mouse_click(BasePageLocators.LOCATOR_COOKIE_ACCEPT_BUTTON)

    @allure.step("Кликаем на логотип Яндекса")
    def click_yandex_logo_button(self):
        self.mouse_click(BasePageLocators.LOCATOR_YANDEX_LOGO)

    @allure.step("Кликаем на логотип Самоката")
    def click_scooter_logo_button(self):
        self.mouse_click(BasePageLocators.LOCATOR_SCOOTER_LOGO)

    @allure.step("Кликаем на кнопку 'Заказать' в хэдере")
    def click_header_order_button(self):
        self.mouse_click(BasePageLocators.LOCATOR_ORDER_BUTTON_HEADER)