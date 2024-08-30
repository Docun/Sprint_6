import allure
from pages.orders_scooter import CheckOrderFirstButton, CheckOrderSecondButton


class TestFirstOrderScooter:
    @allure.title('Проверка оформления заказа после клика по кнопке "Заказать" в шапке сайта')
    def test_complete_order(self, start_from_login_page):
        page = CheckOrderFirstButton(start_from_login_page)
        page.wait_for_load_page_order()
        page.click_button_orders()
        page.fill_field_name()
        page.fill_field_surname()
        page.fill_field_address()
        page.click_field_metro()
        page.fill_paragraph_metro()
        page.fill_field_number()
        page.click_order_next()
        page.click_date()
        page.click_field_bring_order()
        page.click_rental_period()
        page.click_four_day()
        page.click_checkbox_black()
        page.fill_comment_for_courier()
        page.click_button_charter()
        page.wait_for_modal_button_yes()
        page.click_modal_button_yes()
        page.examination_text


class TestSecondOrderScooter:
    @allure.title('Проверка оформления заказа после клика по кнопке "Заказать" по середине сайта')
    def test_complete_order(self, start_from_login_page):
        page = CheckOrderSecondButton(start_from_login_page)
        page.wait_for_load_page_order()
        page.scroll_page_to_button()
        page.click_cokies_now()
        page.click_button_orders()
        page.fill_field_name()
        page.fill_field_surname()
        page.fill_field_address()
        page.click_field_metro()
        page.fill_paragraph_metro()
        page.fill_field_number()
        page.click_order_next()
        page.click_date()
        page.fill_field_bring_order()
        page.click_rental_period()
        page.click_five_day()
        page.click_checkbox_gray()
        page.fill_comment_for_courier()
        page.click_button_charter()
        page.wait_for_modal_button_yes()
        page.click_modal_button_yes()
        page.examination_text