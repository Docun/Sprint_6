from pages.section_Important import CheckSections
from iniconf.curl import base_page

class TestImportntQuestions:
    def test_logo_navigation(self, start_from_login_page):
        page = CheckSections(start_from_login_page)
        url = base_page
        page.open_new_page(url)
        page.wait_for_load_questions()
        page.scroll_page_for_live()
        page.click_cookies_now()
        page.check_how_much_section()
        page.close_and_open_new_page()
        page.scroll_page_for_live()
        page.click_cookies_now()
        page.check_some_scooters_section()
        # page.
        # page.
        # page.
        # page.
        # page.
        # page.
        # page.
        # page.
        # page.
        # page.
        # page.
        # page.
        # page.
        # page.
        # page.
        # page.
        # page.
        # page.
        # page.
        # page.


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



