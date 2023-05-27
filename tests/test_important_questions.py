import pytest

import allure

from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from data import QuestionsDictionary


class TestImportantQuestions:

    @allure.title("Проверка списка вопросов о важном")
    @pytest.mark.parametrize('question_index', [i for i in range(8)])
    def test_answers_for_important_questions(self, question_index, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.scroll_down()
        main_page.check_answers_for_important_questions(question_index)
        actual_result = main_page.find_elements(MainPageLocators.LOCATOR_IMPORTANT_ANSWERS)[question_index].text
        expected_result = QuestionsDictionary.questions_and_answers[main_page.find_elements(
            MainPageLocators.LOCATOR_IMPORTANT_QUESTIONS)[question_index].text]
        assert actual_result == expected_result, 'Некорректный ответ на вопрос'
