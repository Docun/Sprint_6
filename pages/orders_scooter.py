import allure
from pages.base_page import BasePage
from locators.orders_scooter_locators import LocatorsOrder
# from locators.base_page_locators import MainPageLocators

class CheckOrderTwoButton(BasePage):

    def click_main_button_order(self):
        self.click_button(LocatorsOrder.MIDDLE_BUTTON)

    def scroll_and_click_button_order(self):
        self.scroll_to_element(LocatorsOrder.ORDER_BUTTON_TWO)
        self.wait_for_element_visibility(LocatorsOrder.ORDER_BUTTON_TWO)
        self.click_button(LocatorsOrder.ORDER_BUTTON_TWO)

    @allure.step('Вводим имя в поле')
    def fill_field_name(self, name):
        self.entering_text_into_a_field(LocatorsOrder.FIELD_NAME, name)

    @allure.step('Вводим фамилию в поле')
    def fill_field_surname(self, surname):
        self.entering_text_into_a_field(LocatorsOrder.FIELD_SURNAME, surname)

    @allure.step('Вводим адрес в поле')
    def fill_field_address(self, address):
        self.entering_text_into_a_field(LocatorsOrder.FIELD_ADDRESS, address)

    @allure.step('Вводим номер телефона в поле')
    def fill_field_number(self, phone_number):
        self.entering_text_into_a_field(LocatorsOrder.FIELD_NUMBER, phone_number)

    @allure.step('Выбираем пункт метро')
    def fill_paragraph_metro(self):
        self.click_button(LocatorsOrder.FIELD_STATION_METRO)
        self.click_button(LocatorsOrder.PARAGRAPH_METRO)

    @allure.step('Кликаем по полю и выбираем дату из поля про самокаты')
    def click_field_bring_order(self):
        self.click_button(LocatorsOrder.FIELD_BRING_ORDER)
        self.click_button(LocatorsOrder.DATE_TWENTY)

    @allure.step('Кликаем по полю срок аренды и выбираем колличество')
    def click_rental_period(self):
        self.click_button(LocatorsOrder.RENTAL_PERIOD)
        self.click_button(LocatorsOrder.FOUR_DAY)

    @allure.step('Выбираем чекбокс серый')
    def click_checkbox_gray(self):
        self.wait_for_element_visibility(LocatorsOrder.CHECKBOX_GRAY)
        self.click_button(LocatorsOrder.CHECKBOX_GRAY)

    @allure.step('Вписываем комент в поле для коментов доставщику')
    def fill_comment_for_courier(self, comment):
        self.entering_text_into_a_field(LocatorsOrder.COMMENT_FOR_COURIER, comment)

    def click_button_orders(self):
        self.click_button(LocatorsOrder.ORDER_BUTTON_TWO)

    @allure.step('Ждем окно и кликаем по кнопке да')
    def wait_and_click_modal_button_yes(self):
        self.wait_for_element_visibility(LocatorsOrder.ORDERS_YES)
        self.click_button(LocatorsOrder.ORDERS_YES)

    def check_order_text(self):
        element = self.wait_for_element_visibility(LocatorsOrder.ORDERS_CHECK_STATUS)
        return element.text



    @allure.step('Вводим все пользовательские данные для заказа аренды')
    def order_collection(self, name, surname, address, phone_number, comment):
        self.fill_field_name(name)
        self.fill_field_surname(surname)
        self.fill_field_address(address)
        self.fill_paragraph_metro()
        self.fill_field_number(phone_number)
        self.click_button(LocatorsOrder.ORDER_NEXT)
        self.wait_for_element_visibility(LocatorsOrder.INSCRIPTION)
        self.click_field_bring_order()
        self.click_rental_period()
        self.click_checkbox_gray()
        self.fill_comment_for_courier(comment)
        self.click_button_orders()
        self.wait_and_click_modal_button_yes()