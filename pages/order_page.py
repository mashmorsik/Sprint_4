import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.order_page_locators import OrderPageLocators


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполняем поле 'Имя'")
    def set_name(self, name):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.LOCATOR_NAME_FIELD))
        self.driver.find_element(*OrderPageLocators.LOCATOR_NAME_FIELD).send_keys(name)

    @allure.step("Заполняем поле 'Фамилия'")
    def set_surname(self, surname):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.LOCATOR_SURNAME_FIELD))
        self.driver.find_element(*OrderPageLocators.LOCATOR_SURNAME_FIELD).send_keys(surname)

    @allure.step("Заполняем поле 'Адрес'")
    def set_address(self, address):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.LOCATOR_ADDRESS_FIELD))
        self.driver.find_element(*OrderPageLocators.LOCATOR_ADDRESS_FIELD).send_keys(address)

    @allure.step("Выбираем станцию метро")
    def choose_metro_station(self, station):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.LOCATOR_METRO_STATION_FIELD))
        self.driver.find_element(*OrderPageLocators.LOCATOR_METRO_STATION_FIELD).click()
        self.driver.find_element(*OrderPageLocators.LOCATOR_METRO_STATION_FIELD).send_keys(station)
        self.driver.find_element(*OrderPageLocators.LOCATOR_METRO_STATION_FIELD).send_keys(Keys.ARROW_DOWN + Keys.ENTER)

    @allure.step("Заполняем поле 'Номер телефона'")
    def set_phone_number(self, number):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.LOCATOR_PHONE_NUMBER_FIELD))
        self.driver.find_element(*OrderPageLocators.LOCATOR_PHONE_NUMBER_FIELD).send_keys(number)

    @allure.step("Нажимаем 'Далее'")
    def click_next_button(self):
        WebDriverWait(self.driver, 8).until(expected_conditions.element_to_be_clickable(OrderPageLocators.LOCATOR_NEXT_BUTTON))
        self.driver.find_element(*OrderPageLocators.LOCATOR_NEXT_BUTTON).click()

    @allure.step("Выбираем дату доставки")
    def choose_delivery_date(self, date):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.LOCATOR_CHOOSE_DELIVERY_DATE_FIELD))
        self.driver.find_element(*OrderPageLocators.LOCATOR_CHOOSE_DELIVERY_DATE_FIELD).send_keys(date)
        self.driver.find_element(*OrderPageLocators.LOCATOR_CHOOSE_DELIVERY_DATE_FIELD).send_keys(Keys.ENTER)

    @allure.step("Выбираем срок аренды")
    def choose_rent_period(self, period):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.LOCATOR_RENT_PERIOD_FIELD))
        self.driver.find_element(*OrderPageLocators.LOCATOR_RENT_PERIOD_FIELD).click()
        self.driver.find_element(By.XPATH, f'.//div[@class="Dropdown-option" and text()="{period}"]').click()

    @allure.step("Выбираем цвет самоката")
    def choose_scooter_color(self, black=False, grey=False):
        if black:
            self.driver.find_element(*OrderPageLocators.LOCATOR_CHOOSE_SCOOTER_COLOR_BLACK).click()
        if grey:
            self.driver.find_element(*OrderPageLocators.LOCATOR_CHOOSE_SCOOTER_COLOR_GREY).click()

    @allure.step("Оставляем комментарий")
    def leave_comment_for_delivery(self, comment):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.LOCATOR_DELIVERY_COMMENT_FIELD))
        self.driver.find_element(*OrderPageLocators.LOCATOR_DELIVERY_COMMENT_FIELD).send_keys(comment)

    @allure.step("Нажимаем 'Заказать'")
    def click_order_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.LOCATOR_ORDER_BUTTON))
        self.driver.find_element(*OrderPageLocators.LOCATOR_ORDER_BUTTON).click()

    @allure.step("Подтверждаем, что хотим сделать заказ")
    def click_yes_want_to_make_order(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(OrderPageLocators.LOCATOR_YES_ORDER_BUTTON))
        self.driver.find_element(*OrderPageLocators.LOCATOR_YES_ORDER_BUTTON).click()

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