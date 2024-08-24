import pytest
from selenium import webdriver
from pages.section_important import *



class TestSectionHowMuch:
    @pytest.fixture(autouse=True)
    def setup(self, start_from_login_page):
        self.page = CheckHowMuchSection(start_from_login_page)

    def check_much_selection(self):
        self.page.wait_for_load_questions()
        self.page.scroll_page_for_live()
        self.page.click_cokies_now()
        self.page.click_questions()
        self.page.get_text_section_how_much()
        assert "Сутки — 400 рублей. Оплата курьеру — наличными или картой." in get_text_section_how_much
    # @classmethod
    # def setup_class(cls):
    #     # создали драйвер для браузера Firefox
    #     cls.driver = webdriver.Firefox()
    #     cls.driver.maximize_window()
    # def test_check_section_how(self):
    #     # перешли на страницу тестового приложения
    #     self.driver.get('https://qa-scooter.praktikum-services.ru/')
    #
    #     # Объект класса раздела "Сколько стоит"
    #     section_page = HowMuchSection(self.driver)
    #
    #     # Дожидаемся загрузки раздела "Сколько стоит"
    #     section_page.wait_for_load_how_much()
    #
    #     # Прокручиваем страницу
    #     section_page.scroll_page_for_live()
    #
    #     # Кликаем по кукам
    #     section_page.click_cokies_now()
    #
    #     # Кликаем по разделу "Сколько стоит"
    #     section_page.click_how_much()
    #
    #     # Получаем текст из выпадающего раздела
    #     open_section = section_page.get_text_section_how_much()
    #
    #     # Делаем проверку раздела "Сколько стоит"
    #
    # @classmethod
    # def teardown_class(cls):
    #     # Закрой браузер
    #     cls.driver.quit()




class TestSectionScoters:
    @pytest.fixture(autouse=True)
    def setup(self, start_from_login_page):
        self.page = CheckSomeScoters(start_from_login_page)

    def check_selection_scoters(self):
        self.page.wait_for_load_questions()
        self.page.scroll_page_for_live()
        self.page.click_cokies_now()
        self.page.click_questions()
        self.page.get_text_section_how_much()
        assert "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим." in
    # driver = None
    #
    # @classmethod
    # def setup_class(cls):
    #     # создали драйвер для браузера Firefox
    #     cls.driver = webdriver.Firefox()
    #     cls.driver.maximize_window()
    #
    # def test_check_section_scoters(self):
    #     # перешли на страницу тестового приложения
    #     self.driver.get('https://qa-scooter.praktikum-services.ru/')
    #
    #     # Объект класса раздела "Сколько стоит"
    #     section_page = SomeScooters(self.driver)
    #
    #     # Дожидаемся загрузки раздела "Сколько стоит"
    #     section_page.wait_for_load_scoters()
    #
    #     # Прокручиваем страницу
    #     section_page.scroll_page_for_live()
    #
    #     # Кликаем по кукам
    #     section_page.click_cokies_now()
    #
    #     # Кликаем по разделу "Самокаты_шмамокаты"
    #     section_page.click_some_scoters()
    #
    #     # Получаем текст из выпадающего раздела
    #     open_section = section_page.get_text_section_scoters()
    #
    #     # Делаем проверку раздела "Сколько стоит"
    #     assert open_section == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    #
    # @classmethod
    # def teardown_class(cls):
    #     # Закрой браузер
    #     cls.driver.quit()



class TestSectionOrdersNow:
    @pytest.fixture(autouse=True)
    def setup(self, start_from_login_page):
        self.page = CheckResntalTime(start_from_login_page)

    def check_section_orders(self):
        self.page.wait_for_load_questions()
        self.page.scroll_page_for_live()
        self.page.click_cokies_now()
        self.page.click_questions()
        self.page.get_text_section_how_much()
        assert "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30." in
    # driver = None
    #
    # @classmethod
    # def setup_class(cls):
    #     # создали драйвер для браузера Firefox
    #     cls.driver = webdriver.Firefox()
    #     cls.driver.maximize_window()
    #
    # def test_check_section_orders(self):
    #     # перешли на страницу тестового приложения
    #     self.driver.get('https://qa-scooter.praktikum-services.ru/')
    #
    #     # Объект класса раздела "Сколько стоит"
    #     section_page = RentalTime(self.driver)
    #
    #     # Дожидаемся загрузки раздела "Сколько стоит"
    #     section_page.wait_for_load_orders()
    #
    #     # Прокручиваем страницу
    #     section_page.scroll_page_for_live()
    #
    #     # Кликаем по кукам
    #     section_page.click_cokies_now()
    #
    #     # Кликаем по разделу "Про заказ"
    #     section_page.click_some_time_order()
    #
    #     # Получаем текст из выпадающего раздела
    #     open_section = section_page.get_text_section_order()
    #
    #     # Делаем проверку раздела "Оформление заказа"
    #     assert open_section == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    #
    # @classmethod
    # def teardown_class(cls):
    #     # Закрой браузер
    #     cls.driver.quit()



class TestSectionReturnOrder:
    @pytest.fixture(autouse=True)
    def setup(self, start_from_login_page):
        self.page = CheckReturnOrder(start_from_login_page)

    def check_section_orders(self):
        self.page.wait_for_load_questions()
        self.page.scroll_page_for_live()
        self.page.click_cokies_now()
        self.page.click_questions()
        self.page.get_text_section_how_much()

    # @classmethod
    # def setup_class(cls):
    #     # создали драйвер для браузера Firefox
    #     cls.driver = webdriver.Firefox()
    #     cls.driver.maximize_window()
    #
    # def test_check_section_return_orders(self):
    #     # перешли на страницу тестового приложения
    #     self.driver.get('https://qa-scooter.praktikum-services.ru/')
    #
    #     # Объект класса раздела "Сколько стоит"
    #     section_page = ReturnOrder(self.driver)
    #
    #     # Дожидаемся загрузки раздела "вернуть самокат раньше?"
    #     section_page.wait_for_load_orders()
    #
    #     # Прокручиваем страницу
    #     section_page.scroll_page_for_live()
    #
    #     # Кликаем по кукам
    #     section_page.click_cokies_now()
    #
    #     # Кликаем по разделу "Можно ли продлить заказ или вернуть самокат раньше?"
    #     section_page.click_some_return_order()
    #
    #     # Получаем текст из выпадающего раздела
    #     open_section = section_page.get_text_section_order()
    #
    #     # Делаем проверку раздела "Оформление заказа"
    #     assert open_section == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    #
    # @classmethod
    # def teardown_class(cls):
    #     # Закрой браузер
    #     cls.driver.quit()




class TestSectionQuickCharger:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    def test_check_section_quick_charger(self):
        # перешли на страницу тестового приложения
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        # Объект класса раздела "Сколько стоит"
        section_page = QuickCharger(self.driver)

        # Дожидаемся загрузки раздела "вернуть самокат раньше?"
        section_page.wait_for_load_orders()

        # Прокручиваем страницу
        section_page.scroll_page_for_live()

        # Кликаем по кукам
        section_page.click_cokies_now()

        # Кликаем по разделу "Вы привозите зарядку вместе с самокатом?"
        section_page.click_some_time_order()

        # Получаем текст из выпадающего раздела
        open_section = section_page.get_text_section_order()

        # Делаем проверку раздела "Оформление заказа"
        assert open_section == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()



class TestSectionCancelOrders:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    def test_check_section_cancel_order(self):
        # перешли на страницу тестового приложения
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        # Объект класса раздела "Сколько стоит"
        section_page = CancelOrders(self.driver)

        # Дожидаемся загрузки раздела "вернуть самокат раньше?"
        section_page.wait_for_load_orders()

        # Прокручиваем страницу
        section_page.scroll_page_for_live()

        # Кликаем по кукам
        section_page.click_cokies_now()

        # Кликаем по разделу "Можно ли отменить заказ?"
        section_page.click_some_time_order()

        # Получаем текст из выпадающего раздела
        open_section = section_page.get_text_section_order()

        # Делаем проверку раздела "Оформление заказа"
        assert open_section == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()


class TestSectionLiveForMkad:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    def test_check_section_cancel_order(self):
        # перешли на страницу тестового приложения
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        # Объект класса раздела "Сколько стоит"
        section_page = LiveForMkad(self.driver)

        # Дожидаемся загрузки раздела "вернуть самокат раньше?"
        section_page.wait_for_load_orders()

        # Прокручиваем страницу
        section_page.scroll_page_for_live()

        # Кликаем по кукам
        section_page.click_cokies_now()

        # Кликаем по разделу "Я живу за МКАДом, привезёте?"
        section_page.click_section_live_mkad()

        # Получаем текст из выпадающего раздела
        open_section = section_page.get_text_section_live_mkad()

        # Делаем проверку раздела "Оформление заказа"
        assert open_section == "Да, обязательно. Всем самокатов! И Москве, и Московской области."

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()