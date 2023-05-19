from selenium.webdriver.common.by import By


class MainPageLocators:

    LOCATOR_HOME_PAGE_ORDER_BUTTON = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" '
                                                'and text()="Заказать"]') # Кнопка Заказать на Главной странице

    LOCATOR_IMPORTANT_QUESTIONS = (By.XPATH, './/*[contains(@id, "accordion__heading-")]') # Важный вопрос

    LOCATOR_IMPORTANT_ANSWERS = (By.XPATH, './/*[contains(@id, "accordion__panel-")]/p') # Важный ответ

    LOCATOR_IMPORTANT_QUESTIONS_HEADER = (By.XPATH, './/div[text()]="Вопросы о важном"') # Вопросы о важном заголовок

    LOCATOR_SET_OF_QUESTIONS = [By.XPATH, ".//*[@class='accordion']"]  # Поле с вопросами и ответами