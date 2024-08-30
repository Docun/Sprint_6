from locators.selection_important_locators import LocatorsSelection
from locators.base_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class CheckSections(BasePage):

    def click_buttons_cockies(self):
        self.click_button(MainPageLocators.COOKIE_BUTTONS)

    @allure.step('Скролим страницу до последнего раздела в конце страницы')
    def scroll_page_for_live(self):
        self.scroll_to_element(LocatorsSelection.LIVE_FOR_MKAD)

    @allure.step('Меняем локаторы на значение index, ждем блок вопросов о главном и кликаем по ним')
    def check_block_of_questions(self, meaning):
        selector, locator = LocatorsSelection.ALL_QUESTIONS
        locator = locator.format(meaning)
        self.wait_and_click_element((selector, locator))
        return self.wait_and_click_element((selector, locator)).get_attribute("id")

    @allure.step('Получаем видимый текст из поля под вопросом')
    def find_answer(self, meaning):
        selector, locator = LocatorsSelection.ALL_ANSWERS
        locator = locator.format(meaning)
        element = self.wait_for_element_visibility((selector, locator))
        return element.text
