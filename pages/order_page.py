import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Заполняем поле 'Имя'")
    def set_name(self, name):
        self.send_key(OrderPageLocators.LOCATOR_NAME_FIELD, name)

    @allure.step("Заполняем поле 'Фамилия'")
    def set_surname(self, surname):
        self.send_key(OrderPageLocators.LOCATOR_SURNAME_FIELD, surname)

    @allure.step("Заполняем поле 'Адрес'")
    def set_address(self, address):
        self.send_key(OrderPageLocators.LOCATOR_ADDRESS_FIELD, address)

    @allure.step("Выбираем станцию метро")
    def choose_metro_station(self, station):
        self.mouse_click(OrderPageLocators.LOCATOR_METRO_STATION_FIELD)
        self.send_key(OrderPageLocators.LOCATOR_METRO_STATION_FIELD, station)
        self.send_key(OrderPageLocators.LOCATOR_METRO_STATION_FIELD, Keys.ARROW_DOWN + Keys.ENTER)

    @allure.step("Заполняем поле 'Номер телефона'")
    def set_phone_number(self, number):
        self.send_key(OrderPageLocators.LOCATOR_PHONE_NUMBER_FIELD, number)

    @allure.step("Нажимаем 'Далее'")
    def click_next_button(self):
        self.mouse_click(OrderPageLocators.LOCATOR_NEXT_BUTTON)

    @allure.step("Выбираем дату доставки")
    def choose_delivery_date(self, date):
        self.send_key(OrderPageLocators.LOCATOR_CHOOSE_DELIVERY_DATE_FIELD, date)
        self.send_key(OrderPageLocators.LOCATOR_CHOOSE_DELIVERY_DATE_FIELD, Keys.ENTER)

    @allure.step("Выбираем срок аренды")
    def choose_rent_period(self, period):
        self.mouse_click(OrderPageLocators.LOCATOR_RENT_PERIOD_FIELD)
        self.mouse_click((By.XPATH, f'.//div[@class="Dropdown-option" and text()="{period}"]'))

    @allure.step("Выбираем цвет самоката")
    def choose_scooter_color(self, black, grey):
        if black:
            self.mouse_click(OrderPageLocators.LOCATOR_CHOOSE_SCOOTER_COLOR_BLACK)
        if grey:
            self.mouse_click(OrderPageLocators.LOCATOR_CHOOSE_SCOOTER_COLOR_GREY)

    @allure.step("Оставляем комментарий")
    def leave_comment_for_delivery(self, comment):
        self.send_key(OrderPageLocators.LOCATOR_DELIVERY_COMMENT_FIELD, comment)

    @allure.step("Нажимаем 'Заказать'")
    def click_order_button(self):
        self.mouse_click(OrderPageLocators.LOCATOR_ORDER_BUTTON)

    @allure.step("Подтверждаем, что хотим сделать заказ")
    def click_yes_want_to_make_order(self):
        self.mouse_click(OrderPageLocators.LOCATOR_YES_ORDER_BUTTON)

    @allure.step("Оформляем заказ")
    def make_order(self, name, surname, address, station, number, date, period, black, grey, comment):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.choose_metro_station(station)
        self.set_phone_number(number)
        self.click_next_button()

        self.choose_delivery_date(date)
        self.choose_rent_period(period)
        self.choose_scooter_color(black, grey)
        self.leave_comment_for_delivery(comment)
        self.click_order_button()

        self.click_yes_want_to_make_order()
