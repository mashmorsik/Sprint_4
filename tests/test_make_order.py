import pytest
import allure
from selenium import webdriver
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators

from pages.base_page import BasePage
from data import user_1, user_2


class TestMakeOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru')
        base_page = BasePage(cls.driver)
        base_page.accept_cookies()

    @allure.title("Проверка оформления заказа")
    @pytest.mark.parametrize('button, name, surname, address, metro_station, phone_number, rent_date, rent_period,'
                             'black_color, grey_color, comment', [(user_1.button, user_1.name, user_1.surname,
                                                                   user_1.address, user_1.metro_station,
                                                                   user_1.phone_number, user_1.rent_date,
                                                                   user_1.rent_period, user_1.black_color,
                                                                   user_1.grey_color, user_1.comment),
                                                                  (user_2.button, user_2.name, user_2.surname,
                                                                   user_2.address, user_2.metro_station,
                                                                   user_2.phone_number, user_2.rent_date,
                                                                   user_2.rent_period, user_2.black_color,
                                                                   user_2.grey_color, user_2.comment)
                                                                  ])
    def test_make_order_click_header_order_button(self, button, name, surname, address, metro_station, phone_number,
                                                  rent_date, rent_period,
                                                  black_color, grey_color, comment):
        order_page = OrderPage(self.driver)
        self.driver.find_element(*button).click()

        order_page.make_order(name, surname, address, metro_station, phone_number, rent_date, rent_period,
                              black_color, grey_color, comment)

        assert self.driver.find_element(*OrderPageLocators.LOCATOR_SUCCESSFUL_ORDER)

        self.driver.get('https://qa-scooter.praktikum-services.ru'), 'Ошибка во время оформления заказа'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
