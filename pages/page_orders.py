from locators.orders_scooter import LocatorsOrder
from locators.selection_important import LocatorsSelection
from test_base import BasePage


class CheckOrderFirstButton(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.order_button = LocatorsOrder.order_button
        self.field_name = LocatorsOrder.field_name
        self.field_surname = LocatorsOrder.field_surname
        self.field_address = LocatorsOrder.field_address
        self.field_number = LocatorsOrder.field_number
        self.order_next = LocatorsOrder.order_next
        self.field_bring_order = LocatorsOrder.field_bring_order
        self.rental_period = LocatorsOrder.rental_period
        self.four_day = LocatorsOrder.four_day
        self.checkbox_black = LocatorsOrder.checkbox_black
        self.comment_for_courier = LocatorsOrder.comment_for_courier
        self.button_middle = LocatorsOrder.button_middle
        self.order_yes = LocatorsOrder.order_yes
        self.order_check_status = LocatorsOrder.order_check_status
        self.inscription = LocatorsOrder.inscription
        self.field_station_metro = LocatorsOrder.field_station_metro
        self.paragraph_metro = LocatorsOrder.paragraph_metro
        self.date_twenty = LocatorsOrder.date_twenty

    def wait_for_load_page_order(self):
        self.click_button(self.order_button)

    def click_button_orders(self):
        self.click_button(self.order_button)

    def fill_field_name(self, name):
        self.entering_text_into_a_field(self.field_name, name)

    def fill_field_surname(self, surname):
        self.entering_text_into_a_field(self.field_surname, surname)

    def fill_field_address(self, address):
        self.entering_text_into_a_field(self.field_address, address)

    def click_field_metro(self):
        self.click_button(self.field_station_metro)

    def fill_paragraph_metro(self):
        self.click_button(self.paragraph_metro)

    def fill_field_number(self, number):
        self.entering_text_into_a_field(self.field_number, number)

    def wait_for_load_about_rent(self):
        self.wait_for_element_visibility(self.inscription)

    def click_order_next(self):
        self.click_button(self.order_next)

    def click_date(self):
        self.click_button(self.field_bring_order)

    def click_field_bring_order(self):
        self.click_button(self.date_twenty)

    def click_rental_period(self):
        self.click_button(self.rental_period)

    def click_four_day(self):
        self.click_button(self.four_day)

    def click_checkbox_black(self):
        self.click_button(self.checkbox_black)

    def fill_comment_for_courier(self, comment):
        self.entering_text_into_a_field(self.comment_for_courier, comment)

    def click_button_charter(self):
        self.wait_and_click_element(self.button_middle)

    def click_order_yes(self):
        self.driver.click_button(*self.order_yes)

    def examination_text(self, text):
        self.driver.get_text_from_field(self, text)




# Класс для проверки второй кнопки на странице
class CheckOrderSecondButton(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.order_button_two = LocatorsOrder.order_button_two
        self.order_button = LocatorsOrder.order_button
        self.field_name = LocatorsOrder.field_name
        self.field_surname = LocatorsOrder.field_surname
        self.field_address = LocatorsOrder.field_address
        self.field_number = LocatorsOrder.field_number
        self.order_next = LocatorsOrder.order_next
        self.field_bring_order = LocatorsOrder.field_bring_order
        self.rental_period = LocatorsOrder.rental_period
        self.five_day = LocatorsOrder.five_day
        self.checkbox_gray = LocatorsOrder.checkbox_gray
        self.comment_for_courier = LocatorsOrder.comment_for_courier
        self.button_middle = LocatorsOrder.button_middle
        self.order_yes = LocatorsOrder.order_yes
        self.inscription = LocatorsOrder.inscription
        self.field_station_metro = LocatorsOrder.field_station_metro
        self.paragraph_metro_two = LocatorsOrder.paragraph_metro_two
        self.date_thirty = LocatorsOrder.date_thirty
        self.cookie_button = LocatorsSelection.cookie_button
        self.order_check_status = LocatorsOrder.order_check_status

    def wait_for_load_page_order(self):
        self.wait_for_element_visibility(self.order_button)

    def scroll_page_to_button(self):
        self.scroll_to_element(self.order_button_two)

    def click_cokies_now(self):
        self.wait_and_click_element(self.cookie_button)

    def click_button_orders(self):
        self.wait_and_click_element(self.order_button_two)

    def fill_field_name(self, name):
        self.entering_text_into_a_field(self.field_name, name)

    def fill_field_surname(self, surname):
        self.entering_text_into_a_field(self.field_surname, surname)

    def fill_field_address(self, address):
        self.entering_text_into_a_field(self.field_address, address)

    def click_field_metro(self):
        self.wait_and_click_element(self.field_station_metro)

    def fill_paragraph_metro(self):
        self.wait_and_click_element(self.paragraph_metro_two)

    def fill_field_number(self, number):
        self.entering_text_into_a_field(self.field_number, number)

    def wait_for_load_about_rent(self):
        self.wait_for_element_visibility(self.inscription)

    def click_order_next(self):
        self.wait_and_click_element(self.order_next)

    def click_date(self):
        self.wait_and_click_element(self.field_bring_order)

    def fill_field_bring_order(self):
        self.wait_and_click_element(self.date_thirty)

    def click_rental_period(self):
        self.wait_and_click_element(self.rental_period)

    def click_five_day(self):
        self.wait_and_click_element(self.five_day)

    def click_checkbox_gray(self):
        self.wait_and_click_element(self.checkbox_gray)

    def fill_comment_for_courier(self, comment):
        self.entering_text_into_a_field(self.comment_for_courier, comment)

    def click_button_charter(self):
        self.driver.click_button(*self.button_middle)

    def test(self):
        self.wait_for_element_visibility(*self.order_check_status)

    def click_order_yes(self):
        self.driver.wait_and_click_element(*self.order_yes)

    def examination_text(self, text):
        self.driver.get_text_from_field(self, text)


