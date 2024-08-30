from locators.orders_scooter_locators import LocatorsOrder
from locators.selection_important_locators import LocatorsSelection
from pages.base_page import BasePage
from iniconf.data import safe_keeper
import allure

class CheckOrderFirstButton(BasePage):

    @allure.step('Вводим имя в поле')
    def fill_field_name(self, field_name):
        self.entering_text_into_a_field(LocatorsOrder.field_name, safe_keeper['name'])

    @allure.step('Вводим имя в поле')
    def fill_field_surname(self):
        self.entering_text_into_a_field(LocatorsOrder.field_surname, safe_keeper['surname'])

    @allure.step('Вводим фамилию в поле')
    def fill_field_surname(self):
        self.entering_text_into_a_field(LocatorsOrder.field_surname, safe_keeper['surname'])

    @allure.step('Вводим адрес в поле')
    def fill_field_address(self):
        self.entering_text_into_a_field(LocatorsOrder.field_address, safe_keeper['address'])

    @allure.step('Выбираем пункт метро')
    def fill_paragraph_metro(self):
        self.click_button(LocatorsOrder.field_station_metro)
        self.click_button(LocatorsOrder.paragraph_metro)

    @allure.step('Кликаем по полю и выбираем дату из поля про самокаты')
    def click_field_bring_order(self):
        self.click_button(LocatorsOrder.field_bring_order)
        self.click_button(LocatorsOrder.date_twenty)

    @allure.step('Кликаем по полю срок аренды и выбираем колличество')
    def click_rental_period(self):
        self.click_button(LocatorsOrder.rental_period)
        self.click_button(LocatorsOrder.four_day)

    @allure.step('Вписываем комент в поле для коментов доставщику')
    def fill_comment_for_courier(self):
        self.entering_text_into_a_field(LocatorsOrder.comment_for_courier, safe_keeper['comment'])

    @allure.step('Ждем и кликаем модалку с кнопкой да')
    def wait_and_click_modal_button_yes(self):
        self.wait_for_element_visibility(LocatorsOrder.order_yes)
        self.wait_and_click_element(LocatorsOrder.order_yes)








    @allure.step('Кликаем по кнопке Заказать')
    def click_button_orders(self):
        self.click_button(self.order_button)


    @allure.step('Кликаем по кнопке далее')
    def click_order_next(self):
        self.click_button(self.order_next)

    @allure.step('Кликаем по чекбоксу чёрни')
    def click_checkbox_black(self):
        self.click_button(self.checkbox_black)


    @allure.step('Кликаем по кнопке заказать для завершения заказа')
    def click_button_charter(self):
        self.wait_and_click_element(self.button_middle)

    @allure.step('Ищем текст о завершении заказа')
    def examination_text(self):
        self.find_element_by_text_and_verify(self.order_check_status, safe_keeper['check_orders'])





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

    @allure.step('Ждем кнопку Заказать')
    def wait_for_load_page_order(self):
        self.wait_for_element_visibility(self.order_button)

    @allure.step('Скролим до кнопки Заказать с середины страницы')
    def scroll_page_to_button(self):
        self.scroll_to_element(self.order_button_two)

    @allure.step('Кликаем по кнопке что бы скрыть куки')
    def click_cokies_now(self):
        self.wait_and_click_element(self.cookie_button)

    @allure.step('Кликаем по кнопке заказать')
    def click_button_orders(self):
        self.wait_and_click_element(self.order_button_two)

    @allure.step('Вводим имя в поле')
    def fill_field_name(self):
        self.entering_text_into_a_field(self.field_name, safe_keeper['name_1'])

    @allure.step('Вводим фамилию в поле')
    def fill_field_surname(self):
        self.entering_text_into_a_field(self.field_surname, safe_keeper['surname_2'])

    @allure.step('Вводим адрес в поле')
    def fill_field_address(self):
        self.entering_text_into_a_field(self.field_address, safe_keeper['address_3'])

    @allure.step('Кликаем по полю метро')
    def click_field_metro(self):
        self.wait_and_click_element(self.field_station_metro)

    @allure.step('Выбираем элемент с текстом метро')
    def fill_paragraph_metro(self):
        self.wait_and_click_element(self.paragraph_metro_two)

    @allure.step('Вводим номер телефона в поле')
    def fill_field_number(self):
        self.entering_text_into_a_field(self.field_number, safe_keeper['phone_number_4'])

    @allure.step('Кликаем по кнопке далее')
    def click_order_next(self):
        self.wait_and_click_element(self.order_next)

    @allure.step('Кликаем по полю Поле когда привезти самокат')
    def click_date(self):
        self.wait_and_click_element(self.field_bring_order)

    @allure.step('Выбираем дату из выпадающего меню')
    def fill_field_bring_order(self):
        self.wait_and_click_element(self.date_thirty)

    @allure.step('Кликаем по полю срок аренды')
    def click_rental_period(self):
        self.wait_and_click_element(self.rental_period)

    @allure.step('Выбираем дату из поля')
    def click_five_day(self):
        self.wait_and_click_element(self.five_day)

    @allure.step('Выбираем чекбокс серый')
    def click_checkbox_gray(self):
        self.wait_and_click_element(self.checkbox_gray)

    @allure.step('Выбираем чекбокс серый')
    def fill_comment_for_courier(self):
        self.entering_text_into_a_field(self.comment_for_courier, safe_keeper['comment_5'])

    @allure.step('Кликаем по кнопке заказать что бы завершить заказ')
    def click_button_charter(self):
        self.wait_and_click_element(self.button_middle)

    @allure.step('Ждем модалку с кнопкой да')
    def wait_for_modal_button_yes(self):
        self.wait_for_element_visibility(self.order_yes)

    @allure.step('кликаем по кнопке да')
    def click_modal_button_yes(self):
        self.wait_and_click_element(self.order_yes)

    @allure.step('Ищем текст о завершении заказа')
    def examination_text(self):
        self.find_element_by_text_and_verify(self.order_check_status, safe_keeper['check_orders'])
