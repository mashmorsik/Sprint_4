import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.main_page_locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Кликаем на вопрос о важном")
    def check_answers_for_important_questions(self, question_index):
        list_of_questions = self.driver.find_elements(*MainPageLocators.LOCATOR_IMPORTANT_QUESTIONS)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_any_elements_located(MainPageLocators.LOCATOR_IMPORTANT_QUESTIONS))
        list_of_questions[question_index].click()
