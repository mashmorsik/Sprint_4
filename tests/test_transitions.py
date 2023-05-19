import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage


class TestTransitions:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/order')

    @allure.title("Проверка: при нажатии на логотип Самоката попадаем на Главную страницу")
    def test_press_scooter_logo_go_to_main_page(self):
        base_page = BasePage(self.driver)
        base_page.click_scooter_logo_button()
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/', \
            'При нажатии на логотип Самоката не попали на Главную страницу'

    @allure.title("Проверка: при нажатии на логотип Яндекса попадаем на страницу Поиска")
    def test_press_yandex_logo_go_to_yandex_page(self):
        base_page = BasePage(self.driver)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(BasePageLocators.LOCATOR_YANDEX_LOGO))
        base_page.click_yandex_logo_button()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(BasePageLocators.LOCATOR_YANDEX_LOGO))
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(BasePageLocators.LOCATOR_YANDEX_SEARCH))
        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true', 'При нажатии на логотип Яндекса не попали на страницу Поиска'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
