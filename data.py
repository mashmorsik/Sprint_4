from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators


class User:
    def __init__(self, button, name, surname, address, metro_station, phone_number, rent_date, rent_period,
                 black_color, grey_color, comment):
        self.button = button
        self.name = name
        self.surname = surname
        self.address = address
        self.metro_station = metro_station
        self.phone_number = phone_number
        self.rent_date = rent_date
        self.rent_period = rent_period
        self.black_color = black_color
        self.grey_color = grey_color
        self.comment = comment


user_1 = User(BasePageLocators.LOCATOR_ORDER_BUTTON_HEADER, "Игорь", "Орлов", "ул.Красная д.5", "Калужская", "+79998765432",
              "29.05.2023", "сутки", True, True, "Просьба позвонить перед доставкой")

user_2 = User(MainPageLocators.LOCATOR_HOME_PAGE_ORDER_BUTTON, "Ольга", "Ромашкина", "ул.Зеленая д.14", "Белорусская", "+79098765411",
              "26.05.2023", "двое суток", False, True, "Оставьте его у красной скамейки")


class QuestionsDictionary:
    questions_and_answers = {
        "Сколько это стоит? И как оплатить?": "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        "Хочу сразу несколько самокатов! Так можно?": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        "Как рассчитывается время аренды?": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        "Можно ли заказать самокат прямо на сегодня?": "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        "Можно ли продлить заказ или вернуть самокат раньше?": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        "Вы привозите зарядку вместе с самокатом?": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        "Можно ли отменить заказ?": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        "Я жизу за МКАДом, привезёте?": "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    }


class Urls:
    MAIN_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/'
    ORDER_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/order'
