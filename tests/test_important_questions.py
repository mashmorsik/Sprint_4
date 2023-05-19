from selenium import webdriver
import pytest

import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from pages.main_page import MainPage
from data import QuestionsDictionary


class TestImportantQuestions:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')
        base_page = BasePage(cls.driver)
        base_page.accept_cookies()

    @allure.title("Проверка списка вопросов о важном")
    @pytest.mark.parametrize('question_index', [i for i in range(8)])
    def test_answers_for_important_questions(self, question_index):
        main_page = MainPage(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        main_page.check_answers_for_important_questions(question_index)
        actual_result = self.driver.find_elements(*MainPageLocators.LOCATOR_IMPORTANT_ANSWERS)[question_index].text
        expected_result = QuestionsDictionary.questions_and_answers[self.driver.find_elements(*MainPageLocators.LOCATOR_IMPORTANT_QUESTIONS)[question_index].text]
        assert actual_result == expected_result, 'Некорректный ответ на вопрос'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
