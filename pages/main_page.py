import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Кликаем на вопрос о важном")
    def check_answers_for_important_questions(self, question_index):
        base_page = BasePage(self.driver)
        list_of_questions = base_page.find_elements(MainPageLocators.LOCATOR_IMPORTANT_QUESTIONS)
        base_page.wait_element(MainPageLocators.LOCATOR_IMPORTANT_QUESTIONS)
        list_of_questions[question_index].click()
