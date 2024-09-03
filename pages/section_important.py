from locators.selection_important_locators import LocatorsSelection
from pages.base_page import BasePage
import allure


class CheckSections(BasePage):

    @allure.step('Скролим страницу до последнего раздела в конце страницы')
    def scroll_page_for_live(self):
        self.scroll_to_element(LocatorsSelection.LIVE_FOR_MKAD)

    @allure.step('Ждем блок вопросов о главном и кликаем по ним')
    def check_block_of_questions(self, meaning):
        selector, locator = LocatorsSelection.ALL_QUESTIONS
        locator = locator.format(meaning)
        self.wait_for_element_visibility((selector, locator))
        self.click_button((selector, locator))
        return self.wait_for_element_visibility((selector, locator)).get_attribute("id")

    @allure.step('Получаем видимый текст из поля под вопросом')
    def find_answer(self, meaning):
        selector, locator = LocatorsSelection.ALL_ANSWERS
        locator = locator.format(meaning)
        element = self.wait_for_element_visibility((selector, locator))
        return element.text
