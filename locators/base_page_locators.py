from selenium.webdriver.common.by import By


class BasePageLocators:
    # Кнопка принятия куки
    LOCATOR_COOKIE_ACCEPT_BUTTON = (By.XPATH, './/button[text()="да все привыкли"]')

    # Лого Яндекс
    LOCATOR_YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')

    # Лого Самокат
    LOCATOR_SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')

    # Кнопка Заказать в хэдере
    LOCATOR_ORDER_BUTTON_HEADER = (By.XPATH, './/div[@class="Header_Nav__AGCXC"]/button[@class="Button_Button__ra12g"]')

    # Поиск яндекса
    LOCATOR_YANDEX_SEARCH = (By.XPATH, './/iframe[@class="dzen-search-arrow-common__frame" and @aria-label="Поиск Яндекса"]')
