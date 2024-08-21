from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.orders_scooter import Locators_order
from locators.selection_important import Locators_selection
import pytest


# Класс для проверки кнопки заказа из шапки сайта
class CheckOrderFirstButton:
    @pytest.fixture(autouse=True)
    def init_driver(self, browser):
        self.driver = browser

    def __init__(self, driver):
        self.driver = driver
        self.order_button = Locators_order.order_button
        self.field_name = Locators_order.field_name
        self.field_surname = Locators_order.field_surname
        self.field_address = Locators_order.field_address
        self.field_number = Locators_order.field_number
        self.order_next = Locators_order.order_next
        self.field_bring_order = Locators_order.field_bring_order
        self.rental_period = Locators_order.rental_period
        self.four_day = Locators_order.four_day
        self.checkbox_black = Locators_order.checkbox_black
        self.comment_for_courier = Locators_order.comment_for_courier
        self.button_charter = Locators_order.button_charter
        self.order_yes = Locators_order.order_yes
        self.order_check_status = Locators_order.order_check_status
        self.inscription = Locators_order.inscription
        self.field_station_metro = Locators_order.field_station_metro
        self.paragraph_metro = Locators_order.paragraph_metro
        self.date_twenty = Locators_order.date_twenty



    # метод ожидания загрузки страницы
    def wait_for_load_page_order(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.order_button))

    #  Клик по кнопке заказать из шапки страницы
    def click_button_orders(self):
        self.driver.find_element(*self.order_button).click()

    # вводим в поле имя
    def fill_field_name(self):
        name = 'Игорь'
        self.driver.find_element(*Locators_order.field_name).send_keys(name)

    # вводим в поле фамилию
    def fill_field_surename(self):
        surename = 'Жижа'
        self.driver.find_element(*Locators_order.field_surname).send_keys(surename)

    # вводим в поле адрес
    def fill_field_address(self):
        address = 'Пушкина-калатушкина'
        self.driver.find_element(*Locators_order.field_address).send_keys(address)

    # кликаем по полю станция метро
    def click_field_metro(self):
        self.driver.find_element(*self.field_station_metro).click()

    # выбираем метро
    def fill_paragraph_metro(self):
        self.driver.find_element(*self.paragraph_metro).click()

    # вводим в поле номер
    def fill_field_number(self):
        number = '89224194190'
        self.driver.find_element(*Locators_order.field_number).send_keys(number)

    # метод ожидания загрузки страницы
    def wait_for_load_about_rent(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.inscription))

    # кликаем по кнопке дальше
    def click_order_next(self):
        self.driver.find_element(*self.order_next).click()


    def click_date(self):
        self.driver.find_element(*self.field_bring_order).click()

    # вводим в поле дату
    def fill_field_bring_order(self):
        self.driver.find_element(*self.date_twenty).click()

    # выбираем период заказа
    def click_rental_period(self):
        self.driver.find_element(*self.rental_period).click()

    # кликаем по пункту пять дней
    def click_four_day(self):
        self.driver.find_element(*self.four_day).click()

    # выбираем цвет самоката
    def click_checkbox_black(self):
        self.driver.find_element(*self.checkbox_black).click()

    # вводим в поле комент для курьера
    def fill_comment_for_courier(self):
        comment = 'чхз'
        self.driver.find_element(*Locators_order.comment_for_courier).send_keys(comment)

    # завершаем заказ кликаем по кнопке заказать
    def click_button_charter(self):
        self.driver.find_element(*self.button_charter).click()

    # кликаем по пнопке да
    def click_order_yes(self):
        self.driver.find_element(*self.order_yes).click()

    # получаем текст из выпадающего раздела
    def get_text_order_check_status(self):
        return self.driver.find_element(*self.order_check_status).text


# Класс для проверки второй кнопки на странице
class CheckOrderSecondButton:
    def __init__(self, driver):
        self.driver = driver
        self.order_button_two = Locators_order.order_button_two
        self.order_button = Locators_order.order_button
        self.field_name = Locators_order.field_name
        self.field_surname = Locators_order.field_surname
        self.field_address = Locators_order.field_address
        self.field_number = Locators_order.field_number
        self.order_next = Locators_order.order_next
        self.field_bring_order = Locators_order.field_bring_order
        self.rental_period = Locators_order.rental_period
        self.five_day = Locators_order.five_day
        self.checkbox_gray = Locators_order.checkbox_gray
        self.comment_for_courier = Locators_order.comment_for_courier
        self.button_charter = Locators_order.button_charter
        self.order_yes = Locators_order.order_yes
        self.order_check_status = Locators_order.order_check_status
        self.inscription = Locators_order.inscription
        self.field_station_metro = Locators_order.field_station_metro
        self.paragraph_metro_two = Locators_order.paragraph_metro_two
        self.date_thirty = Locators_order.date_thirty
        self.cookie_button = Locators_selection.cookie_button


    # метод ожидания загрузки страницы
    def wait_for_load_page_order(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.order_button))

    # метод для прокрутки страницы до нужного элемента
    def scroll_page_to_button(self):
        element = self.driver.find_element(*self.order_button_two)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.send_keys(self.order_button_two)

    def click_cokies_now(self):
        self.driver.find_element(*self.cookie_button).click()

    #  Клик по кнопке заказать из шапки страницы
    def click_button_orders(self):
        self.driver.find_element(*self.order_button_two).click()

    # вводим в поле имя
    def fill_field_name(self):
        name = 'Жора'
        self.driver.find_element(*Locators_order.field_name).send_keys(name)

    # вводим в поле фамилию
    def fill_field_surename(self):
        surename = 'Бичеслав'
        self.driver.find_element(*Locators_order.field_surname).send_keys(surename)

    # вводим в поле адрес
    def fill_field_address(self):
        address = 'Гагаагага'
        self.driver.find_element(*Locators_order.field_address).send_keys(address)

    # кликаем по полю станция метро
    def click_field_metro(self):
        self.driver.find_element(*self.field_station_metro).click()

    # выбираем метро
    def fill_paragraph_metro(self):
        self.driver.find_element(*self.paragraph_metro_two).click()

    # вводим в поле номер
    def fill_field_number(self):
        number = '+79969969996'
        self.driver.find_element(*Locators_order.field_number).send_keys(number)

    # метод ожидания загрузки страницы
    def wait_for_load_about_rent(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.inscription))

    # кликаем по кнопке дальше
    def click_order_next(self):
        self.driver.find_element(*self.order_next).click()

    # кликаем по полю
    def click_date(self):
        self.driver.find_element(*self.field_bring_order).click()

    # выбираем дату
    def fill_field_bring_order(self):
        self.driver.find_element(*self.date_thirty).click()

    # выбираем период заказа
    def click_rental_period(self):
        self.driver.find_element(*self.rental_period).click()

    # кликаем по пункту четыре дня
    def click_five_day(self):
        self.driver.find_element(*self.five_day).click()

    # выбираем цвет самоката
    def click_checkbox_gray(self):
        self.driver.find_element(*self.checkbox_gray).click()

    # вводим в поле комент для курьера
    def fill_comment_for_courier(self):
        comment = 'чхз'
        self.driver.find_element(*Locators_order.comment_for_courier).send_keys(comment)

    # завершаем заказ кликаем по кнопке заказать
    def click_button_charter(self):
        self.driver.find_element(*self.button_charter).click()

    # кликаем по пнопке да
    def click_order_yes(self):
        self.driver.find_element(*self.order_yes).click()

    # получаем текст из выпадающего раздела
    def get_text_order_check_status(self):
        return self.driver.find_element(*self.order_check_status).text











