import allure

from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data import Urls


class TestTransitions:

    @allure.title("Проверка: при нажатии на логотип Самоката попадаем на Главную страницу")
    def test_press_scooter_logo_go_to_main_page(self, driver):
        base_page = BasePage(driver)
        driver.get(Urls.ORDER_PAGE_URL)
        base_page.click_scooter_logo_button()
        assert base_page.find_element(MainPageLocators.LOCATOR_SCOOTER_TITLE_MAIN_PAGE), \
            'При нажатии на логотип Самоката не попали на Главную страницу'

    @allure.title("Проверка: при нажатии на логотип Яндекса попадаем на страницу Поиска")
    def test_press_yandex_logo_go_to_yandex_page(self, driver):
        base_page = BasePage(driver)
        base_page.click_yandex_logo_button()
        base_page.wait_element(BasePageLocators.LOCATOR_YANDEX_LOGO)
        driver.switch_to.window(driver.window_handles[1])
        assert base_page.find_element(BasePageLocators.LOCATOR_YANDEX_SEARCH), \
            'При нажатии на логотип Яндекса не попали на страницу Поиска'
