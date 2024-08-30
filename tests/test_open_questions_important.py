from pages.section_important import CheckSections
from iniconf.data import safe_keeper
import pytest


class TestImportntQuestions:
    @pytest.mark.parametrize("meaning, get_answer", [(0, safe_keeper[0]), (1, safe_keeper[1]), (2, safe_keeper[2]), (3, safe_keeper[3]), (4, safe_keeper[4]), (5, safe_keeper[5]), (6, safe_keeper[6]), (7, safe_keeper[7])])
    def test_questions_navigation(self, start_from_login_page, meaning, get_answer):
        check_selections = CheckSections(start_from_login_page)
        check_selections.click_buttons_cockies()
        check_selections.scroll_page_for_live()
        check_question = check_selections.check_block_of_questions(meaning)
        get_text = check_selections.find_answer(meaning)
        assert get_answer[check_question] == get_text






# import allure
# from pages.section_important import *
#
# class TestSectionHowMuch:
#     @allure.title('Проверка выпадающего меню (Сколько это стоит? И как оплатить?)')
#     def test_check_much_selection(self, start_from_login_page):
#         page = CheckHowMuchSection(start_from_login_page)
#         page.wait_for_load_questions()
#         page.scroll_page_for_live()
#         page.click_cokies_now()
#         page.click_questions()
#         page.examination_text()
#
#
# class TestSectionScoters:
#     @allure.title('Проверка выпадающего меню (Хочу сразу несколько самокатов! Так можно?)')
#     def test_check_selection_scoters(self, start_from_login_page):
#         page = CheckSomeScoters(start_from_login_page)
#         page.wait_for_load_questions()
#         page.scroll_page_for_live()
#         page.click_cockies_now()
#         page.click_questions()
#         page.examination_text()
#
#
#
# class TestSectionOrdersNow:
#
#     @allure.title('Проверка выпадающего меню (Как рассчитывается время аренды?)')
#     def test_check_section_orders(self, start_from_login_page):
#         page = CheckResntalTime(start_from_login_page)
#         page.wait_for_load_questions()
#         page.scroll_page_for_live()
#         page.click_cockies_now()
#         page.click_questions()
#         page.examination_text()
#
#
#
# class TestSectionReturnOrder:
#     @allure.title('Проверка выпадающего меню (Можно ли продлить заказ или вернуть самокат раньше?)')
#     def test_check_section_orders(self, start_from_login_page):
#         page = CheckReturnOrder(start_from_login_page)
#         page.wait_for_load_questions()
#         page.scroll_page_for_live()
#         page.click_cockies_now()
#         page.click_questions()
#         page.examination_text()
#
#
# class TestSectionQuickCharger:
#     @allure.title('Проверка выпадающего меню (Вы привозите зарядку вместе с самокатом?)')
#     def test_check_section_orders(self, start_from_login_page):
#         page = CheckQuickCharger(start_from_login_page)
#         page.wait_for_load_questions()
#         page.scroll_page_for_live()
#         page.click_cockies_now()
#         page.click_questions()
#         page.examination_text()
#
#
# class TestSectionCancelOrders:
#     @allure.title('Проверка выпадающего меню (Можно ли отменить заказ?)')
#     def test_check_section_orders(self, start_from_login_page):
#         page = CheckCancelOrders(start_from_login_page)
#         page.wait_for_load_questions()
#         page.scroll_page_for_live()
#         page.click_cockies_now()
#         page.click_questions()
#         page.examination_text()
#
#
# class TestSectionLiveForMkad:
#     @allure.title('Проверка выпадающего меню (Я жизу за МКАДом, привезёте?)')
#     def test_check_section_orders(self, start_from_login_page):
#         page = CheckLiveForMkad(start_from_login_page)
#         page.wait_for_load_questions()
#         page.scroll_page_for_live()
#         page.click_cockies_now()
#         page.click_questions()
#         page.examination_text()
#
#
# class TestSectionOrderToday:
#     @allure.title('Проверка выпадающего меню (Можно ли заказать самокат прямо на сегодня?)')
#     def test_check_section_orders(self, start_from_login_page):
#         page = CheckOrderToday(start_from_login_page)
#         page.wait_for_load_questions()
#         page.scroll_page_for_live()
#         page.click_cockies_now()
#         page.click_questions()
#         page.examination_text()



