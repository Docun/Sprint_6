from locators.selection_important import LocatorsSelection
from locators.orders_scooter import LocatorsOrder
from pages.BasePage import BasePage
from iniconf.data import safe_keeper
import allure

class CheckSections(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.accordeon_huw_much = LocatorsSelection.accordeon_huw_much
        self.open_content_how_much = LocatorsSelection.open_content_how_much
        self.accordeon_live_for_mkad = LocatorsSelection.accordeon_live_for_mkad
        self.accordion_some = LocatorsSelection.accordion_some
        self.open_content_some = LocatorsSelection.open_content_some
        self.accordion_rental = LocatorsSelection.accordion_rental
        self.open_content_order = LocatorsSelection.open_content_order
        self.cookie_button = LocatorsSelection.cookie_button
        self.order_button = LocatorsOrder.order_button

    # Общие методы
    @allure.step('Открываем новую страницу и закрываем старую')
    def open_new_page(self, url):
        if self.driver.current_url != url:
            self.driver.get(url)

        if len(self.driver.window_handles) > 1:
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

    @allure.step('Закрываем текущую страницу и открываем новую')
    def close_and_open_new_page(self, url):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(url)

    @allure.step('Проверяем что страница открылась')
    def wait_for_load_questions(self):
        self.wait_for_element_visibility(self.order_button)

    @allure.step('Скролим страницу до последнего раздела в конце страницы')
    def scroll_page_for_live(self):
        self.scroll_to_element(self.accordeon_live_for_mkad)

    @allure.step('Кликаем по кнопке куки')
    def click_cookies_now(self):
        self.click_button(self.cookie_button)

    @allure.step('Кликаем по разделу "Сколько стоит" и проверяем текст')
    def check_how_much_section(self):
        self.click_button(self.accordeon_huw_much)
        self.find_element_by_text_and_verify(self.open_content_how_much, safe_keeper['answer_1'])

    @allure.step('Кликаем по разделу "Хочу сразу несколько самокатов! Так можно?" и проверяем текст')
    def check_some_scooters_section(self):
        self.click_button(self.accordion_some)
        self.find_element_by_text_and_verify(self.open_content_some, safe_keeper['answer_2'])

    @allure.step('Кликаем по разделу "Как рассчитывается время аренды?" и проверяем текст')
    def check_rental_time_section(self):
        self.click_button(self.accordion_rental)
        self.find_element_by_text_and_verify(self.open_content_order, safe_keeper['answer_3'])

    @allure.step('Кликаем по разделу "Класс для проверки раздела "Можно ли продлить заказ или вернуть самокат раньше?" и проверяем текст')
    def check_return_order(self):
        self.click_button(self.accordion_return)
        self.find_element_by_text_and_verify(self.open_content_beautiful_number, safe_keeper['answer_4'])

    @allure.step('Кликаем по разделу "Класс для проверки раздела "Вы привозите зарядку вместе с самокатом?" и проверяем текст')
    def check_quick_charger(self):
        self.click_button(self.accordion_charger)
        self.find_element_by_text_and_verify(self.open_content_full_energy, safe_keeper['answer_5'])
    @allure.step('Кликаем по разделу "Можно ли отменить заказ?" и проверяем текст')
    def check_cancel_orders(self):
        self.click_button(self.accordion_cancel_order)
        self.find_element_by_text_and_verify(self.open_content_no_penalty, safe_keeper['answer_6'])

    @allure.step('Кликаем по разделу "Я живу за МКАДом, привезёте?" и проверяем текст')
    def check_live_for_mkad(self):
        self.click_button(self.accordeon_live_for_mkad)
        self.find_element_by_text_and_verify(self.open_content_live_for_mkad, safe_keeper['answer_7'])

    @allure.step('Кликаем по разделу "Можно ли заказать самокат прямо на сегодня?" и проверяем текст')
    def check_order_today(self):
        self.click_button(self.accordion_rental_now)
        self.find_element_by_text_and_verify(self.open_content_order_more_quickly, safe_keeper['answer_8'])


