from pages.navigation_by_logo import *
from selenium import webdriver



class TestClickByYandex:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    def test_check_click_logo_yandex(self):
        # Перешли на страницу тестового приложения
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        # Объект класса лого Yandex
        logo_yandex = ClickYandexLogo(self.driver)

        # Дожидаемся загрузки раздела "Сколько стоит"
        logo_yandex.wait_for_load_logo()

        # Кликаем по logo yandex
        logo_yandex.click_by_logo_yandex()

        # Ждем пока откроется новое окно
        logo_yandex.wait_for_navigation()

        # Получаем дескрипторы всех открытых окон
        windows = self.driver.window_handles

        # Переключаемся на новое окно (предполагаем, что изначально было одно окно)
        self.driver.switch_to.window(windows[1])

        # Ожидаем переход на нужный сайт
        WebDriverWait(self.driver, 10).until(EC.url_contains('https://dzen.ru/?yredirect=true'))

        # Проверяем, что текущий URL соответствует ожидаемому
        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true'

        # Закрываем новую вкладку и возвращаемся на первоначальную
        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()



class TestClickByScooter:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    def test_check_click_logo_scooter(self):
        # перешли на страницу тестового приложения
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        # Объект класса лого Scooter
        logo_scooter = ClickScootersLogo(self.driver)

        # Ждем загрузку страницы
        logo_scooter.wait_for_load_logo()

        # кликаем по кнопке Заказать
        logo_scooter.click_by_button_order()

        # Кликаем по лого Самокат
        logo_scooter.click_by_logo_scooter()

        # Ждем загрузку страницы
        logo_scooter.wait_navigation_base_page()

        # Проверяем, что текущий URL соответствует ожидаемому
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()




