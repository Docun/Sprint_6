import pytest
from pages.page_orders import CheckOrderFirstButton, CheckOrderSecondButton


class TestFirstOrderScooter:
    @pytest.fixture(autouse=True)
    def setup(self, start_from_login_page):
        self.page = CheckOrderFirstButton(start_from_login_page)

    def test_complete_order(self):
        self.page.wait_for_load_page_order()
        self.page.click_button_orders()
        self.page.fill_field_name('ЫСВМА')
        self.page.fill_field_surname('Жижа')
        self.page.fill_field_address('Пушкина-калатушкина')
        self.page.click_field_metro()
        self.page.fill_paragraph_metro()
        self.page.fill_field_number('89224194190')
        self.page.wait_for_load_about_rent()
        self.page.click_order_next()
        self.page.click_date()
        self.page.click_field_bring_order()
        self.page.click_rental_period()
        self.page.click_four_day()
        self.page.click_checkbox_black()
        self.page.fill_comment_for_courier('чхз')
        self.page.click_button_charter()
        self.page.click_order_yes()
        self.page.examination_text()
        check_text = self.page.order_check_status()
        assert "Заказ оформлен" in check_text


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
        self.page.wait_for_load_about_rent()
        self.page.click_order_next()
        self.page.click_date()
        self.page.fill_field_bring_order()
        self.page.click_rental_period()
        self.page.click_five_day()
        self.page.click_checkbox_gray()
        self.page.fill_comment_for_courier('чхз')
        self.page.click_button_charter()
        self.page.test()
        self.page.click_order_yes()
        self.page.examination_text()
        check_text = self.page.order_check_status()
        assert "Заказ оформлен" in check_text



# class TestCheckFirstButtonOrder:
#     driver = None
#
#     @classmethod
#     def setup_class(cls):
#         # создали драйвер для браузера Firefox
#         cls.driver = webdriver.Firefox()
#         cls.driver.maximize_window()
#
#     def test_check_order_first_button(self):
#         # перешли на страницу тестового приложения
#         self.driver.get(base_page)
#
#         # Объект класса раздела кнопки из шапки сайта
#         first_button = RentScooterPage(self.driver)
#
#         # Дожидаемся загрузки страницы
#         first_button.wait_for_load_page_order()
#
#         # клик по кнопке заказать
#         first_button.click_button_orders()
#
#         # вводим в поле имя
#         first_button.fill_field_name()
#
#         # вводим в поле фамилию
#         first_button.fill_field_surename()
#
#         # вводим в поле адрес
#         first_button.fill_field_address()
#
#         # кликаем по полю метро
#         first_button.click_field_metro()
#
#         # выбираем метро
#         first_button.fill_paragraph_metro()
#
#         # вводим в поле номер
#         first_button.fill_field_number()
#
#         # кликаем по кнопке дальше
#         first_button.click_order_next()
#
#         first_button.click_date()
#
#         # вводим в поле дату
#         first_button.fill_field_bring_order()
#
#         # выбираем период заказа
#         first_button.click_rental_period()
#
#         # кликаем по пункту четыре дня
#         first_button.click_four_day()
#
#         # выбираем цвет самоката
#         first_button.click_checkbox_black()
#
#         # вводим в поле комент для курьера
#         first_button.fill_comment_for_courier()
#
#         # завершаем заказ кликаем по кнопке заказать
#         first_button.click_button_charter()
#
#         # кликаем по пнопке да
#         first_button.click_order_yes()
#
#         # получаем текст из выпадающего раздела
#         end_order = first_button.get_text_order_check_status()
#
#         # Делаем проверку раздела "Оформление заказа"
#         assert "Заказ оформлен" in end_order
#
#     @classmethod
#     def teardown_class(cls):
#         # Закрой браузер
#         cls.driver.quit()



# class TestCheckSecondButtonOrder:
#     driver = None
#
#     @classmethod
#     def setup_class(cls):
#         # создали драйвер для браузера Firefox
#         cls.driver = webdriver.Firefox()
#         cls.driver.maximize_window()
#
#     def test_check_order_first_button(self):
#         # перешли на страницу тестового приложения
#         self.driver.get(base_page)
#
#         # Объект класса раздела кнопки из шапки сайта
#         second_button = CheckOrderSecondButton(self.driver)
#
#         # Дожидаемся загрузки страницы
#         second_button.wait_for_load_page_order()
#
#         second_button.click_cokies_now()
#
#         # скролим до кнопки загрузка
#         second_button.scroll_page_to_button()
#
#         # кликаем по кнопке заказать
#         second_button.click_button_orders()
#
#         # вводим в поле имя
#         second_button.fill_field_name()
#
#         # вводим в поле фамилию
#         second_button.fill_field_surename()
#
#         # вводим в поле адрес
#         second_button.fill_field_address()
#
#         # кликаем по полю метро
#         second_button.click_field_metro()
#
#         # выбираем метро
#         second_button.fill_paragraph_metro()
#
#         # вводим в поле номер
#         second_button.fill_field_number()
#
#         # кликаем по кнопке дальше
#         second_button.click_order_next()
#
#         second_button.click_date()
#
#         # вводим в поле дату
#         second_button.fill_field_bring_order()
#
#         # выбираем период заказа
#         second_button.click_rental_period()
#
#         # кликаем по пункту четыре дня
#         second_button.click_five_day()
#
#         # выбираем цвет самоката
#         second_button.click_checkbox_gray()
#
#         # вводим в поле комент для курьера
#         second_button.fill_comment_for_courier()
#
#         # завершаем заказ кликаем по кнопке заказать
#         second_button.click_button_charter()
#
#         # кликаем по пнопке да
#         second_button.click_order_yes()
#
#         # получаем текст из выпадающего раздела
#         end_order = second_button.get_text_order_check_status()
#
#         # Делаем проверку раздела "Оформление заказа"
#         assert "Заказ оформлен" in end_order
#
#     @classmethod
#     def teardown_class(cls):
#         # Закрой браузер
#         cls.driver.quit()