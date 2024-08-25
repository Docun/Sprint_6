import time

import pytest
from pages.section_important import *

class TestSectionHowMuch:
    @pytest.fixture(autouse=True)
    def setup(self, start_from_login_page):
        self.page = CheckHowMuchSection(start_from_login_page)
    def test_check_much_selection(self):
        self.page.wait_for_load_questions()
        self.page.scroll_page_for_live()
        self.page.click_cokies_now()
        self.page.click_questions()
        self.page.examination_text()


class TestSectionScoters:
    @pytest.fixture(autouse=True)
    def setup(self, start_from_login_page):
        self.page = CheckSomeScoters(start_from_login_page)

    def test_check_selection_scoters(self):
        self.page.wait_for_load_questions()
        self.page.scroll_page_for_live()
        self.page.click_cockies_now()
        self.page.click_questions()
        self.page.examination_text()



class TestSectionOrdersNow:
    @pytest.fixture(autouse=True)
    def setup(self, start_from_login_page):
        self.page = CheckResntalTime(start_from_login_page)

    def test_check_section_orders(self):
        self.page.wait_for_load_questions()
        self.page.scroll_page_for_live()
        self.page.click_cockies_now()
        self.page.click_questions()
        self.page.examination_text()



class TestSectionReturnOrder:
    @pytest.fixture(autouse=True)
    def setup(self, start_from_login_page):
        self.page = CheckReturnOrder(start_from_login_page)

    def test_check_section_orders(self):
        self.page.wait_for_load_questions()
        self.page.scroll_page_for_live()
        self.page.click_cockies_now()
        self.page.click_questions()
        self.page.examination_text()


class TestSectionQuickCharger:
    @pytest.fixture(autouse=True)
    def setup(self, start_from_login_page):
        self.page = CheckQuickCharger(start_from_login_page)

    def test_check_section_orders(self):
        self.page.wait_for_load_questions()
        self.page.scroll_page_for_live()
        self.page.click_cockies_now()
        self.page.click_questions()
        self.page.examination_text()

class TestSectionCancelOrders:
    @pytest.fixture(autouse=True)
    def setup(self, start_from_login_page):
        self.page = CheckCancelOrders(start_from_login_page)

    def test_check_section_orders(self):
        self.page.wait_for_load_questions()
        self.page.scroll_page_for_live()
        self.page.click_cockies_now()
        self.page.click_questions()
        self.page.examination_text()

class TestSectionLiveForMkad:
    @pytest.fixture(autouse=True)
    def setup(self, start_from_login_page):
        self.page = CheckLiveForMkad(start_from_login_page)

    def test_check_section_orders(self):
        self.page.wait_for_load_questions()
        self.page.scroll_page_for_live()
        self.page.click_cockies_now()
        self.page.click_questions()
        self.page.examination_text()

class TestSectionOrderToday:
    @pytest.fixture(autouse=True)
    def setup(self, start_from_login_page):
        self.page = CheckOrderToday(start_from_login_page)

    def test_check_section_orders(self):
        self.page.wait_for_load_questions()
        self.page.scroll_page_for_live()
        self.page.click_cockies_now()
        self.page.click_questions()
        self.page.examination_text()



