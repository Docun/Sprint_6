import pytest
from pages.page_orders import CheckOrderFirstButton, CheckOrderSecondButton


class TestFirstOrderScooter:
    @pytest.fixture(autouse=True)
    def setup(self, start_from_login_page):
        self.page = CheckOrderFirstButton(start_from_login_page)

    def test_complete_order(self):
        self.page.wait_for_load_page_order()
        self.page.click_button_orders()
        self.page.fill_field_name('Жора')
        self.page.fill_field_surname('Жижа')
        self.page.fill_field_address('Пушкина-калатушкина')
        self.page.click_field_metro()
        self.page.fill_paragraph_metro()
        self.page.fill_field_number('89224194190')
        self.page.click_order_next()
        self.page.click_date()
        self.page.click_field_bring_order()
        self.page.click_rental_period()
        self.page.click_four_day()
        self.page.click_checkbox_black()
        self.page.fill_comment_for_courier('Самослав')
        self.page.click_button_charter()
        self.page.wait_for_modal_button_yes()
        self.page.click_modal_button_yes()
        self.page.examination_text


class TestSecondOrderScooter:
    @pytest.fixture(autouse=True)
    def setup(self, start_from_login_page):
        self.page = CheckOrderSecondButton(start_from_login_page)

    def test_complete_order(self):
        self.page.wait_for_load_page_order()
        self.page.scroll_page_to_button()
        self.page.click_cokies_now()
        self.page.click_button_orders()
        self.page.fill_field_name('Жора')
        self.page.fill_field_surname('Бичеслав')
        self.page.fill_field_address('Гагаагага')
        self.page.click_field_metro()
        self.page.fill_paragraph_metro()
        self.page.fill_field_number('+79969969996')
        self.page.click_order_next()
        self.page.click_date()
        self.page.fill_field_bring_order()
        self.page.click_rental_period()
        self.page.click_five_day()
        self.page.click_checkbox_gray()
        self.page.fill_comment_for_courier('Бомба')
        self.page.click_button_charter()
        self.page.wait_for_modal_button_yes
        self.page.click_modal_button_yes()
        self.page.examination_text()