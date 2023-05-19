import allure
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Принимаем куки")
    def accept_cookies(self):
        self.driver.find_element(*BasePageLocators.LOCATOR_COOKIE_ACCEPT_BUTTON).click()

    @allure.step("Кликаем на логотип Яндекса")
    def click_yandex_logo_button(self):
        self.driver.find_element(*BasePageLocators.LOCATOR_YANDEX_LOGO).click()

    @allure.step("Кликаем на логотип Самоката")
    def click_scooter_logo_button(self):
        self.driver.find_element(*BasePageLocators.LOCATOR_SCOOTER_LOGO).click()

    @allure.step("Кликаем на кнопку 'Заказать' в хэдере")
    def click_header_order_button(self):
        self.driver.find_element(*BasePageLocators.LOCATOR_ORDER_BUTTON_HEADER).click()