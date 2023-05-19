from selenium.webdriver.common.by import By


class OrderPageLocators:

    LOCATOR_NAME_FIELD = (By.XPATH, './/input[@placeholder="* Имя"]')     # Поле Имя
    LOCATOR_SURNAME_FIELD = (By.XPATH, './/input[@placeholder="* Фамилия"]')    # Поле Фамилия
    LOCATOR_ADDRESS_FIELD = (By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]')     # Поле Адрес
    LOCATOR_METRO_STATION_FIELD = (By.XPATH, './/input[@placeholder="* Станция метро"]')     # Поле Станция метро
    LOCATOR_PHONE_NUMBER_FIELD = (By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]')     # Поле Телефон

    LOCATOR_NEXT_BUTTON = (By.XPATH, './/button[text()="Далее"]')    # Кнопка Далее

    LOCATOR_CHOOSE_DELIVERY_DATE_FIELD = (By.XPATH, './/input[@placeholder="* Когда привезти самокат"]')    # Поле Когда привезти самокат
    LOCATOR_RENT_PERIOD_FIELD = (By.XPATH, './/div[text()="* Срок аренды"]') # Поле Срок аренды
    LOCATOR_CHOOSE_SCOOTER_COLOR_BLACK = (By.ID, 'black')     # Цвет самоката - Черный
    LOCATOR_CHOOSE_SCOOTER_COLOR_GREY = (By.ID, 'grey')     # Цвет самоката - Серый
    LOCATOR_DELIVERY_COMMENT_FIELD = (By.XPATH, './/input[@placeholder="Комментарий для курьера"]')     # Поле Комментарий для курьера

    LOCATOR_BACK_BUTTON = (By.XPATH, './/button[text()="Назад"]')    # Кнопка Назад
    LOCATOR_ORDER_BUTTON = (By.XPATH, './/*[contains(@class, "Button_Button__ra12g Button_Middle__1CSJM") and text()="Заказать"]')    # Кнопка Заказать

    LOCATOR_MAKE_ORDER_POP_UP = (By.XPATH, './/div[text()="Хотите оформить заказ?"]')
    LOCATOR_YES_ORDER_BUTTON = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Да"]')     # Хотите оформить заказ - кнопка Да
    LOCATOR_NO_ORDER_BUTTON = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Нет"]')  # Хотите оформить заказ - кнопка Нет
    LOCATOR_SUCCESSFUL_ORDER = (By.XPATH, './/*[@class="Order_ModalHeader__3FDaJ"]')




