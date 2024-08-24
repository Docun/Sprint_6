# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from locators.logo_page import LocatorsLogo
# from locators.orders_scooter import LocatorsOrder
# from selenium.webdriver.support import expected_conditions as EC
#
#
# # Класс для проверки перехода по логу яндекса на дзен
# class ClickYandexLogo:
#     def __init__(self, driver):
#         self.driver = driver
#         self.yandex_logo = LocatorsLogo.yandex_logo
#
#         # метод ожидания загрузки страницы
#     def wait_for_load_logo(self):
#         WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.yandex_logo))
#
#     def click_by_logo_yandex(self):
#         WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.yandex_logo)).click()
#
#     def wait_for_navigation(self):
#         WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
#
#
# # Класс для проверки перехода по логу самоката на страницу самоката
# class ClickScootersLogo:
#     def __init__(self, driver):
#         self.driver = driver
#         self.scooter_logo = LocatorsLogo.scooter_logo
#         self.order_button = LocatorsOrder.order_button
#
#     # метод ожидания загрузки страницы
#     def wait_for_load_logo(self):
#         WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.scooter_logo))
#
#     # кликаем по кнопке Заказать
#     def click_by_button_order(self):
#         self.driver.find_element(*self.order_button).click()
#
#     # кликаем по лого Самокат
#     def click_by_logo_scooter(self):
#         self.driver.find_element(*self.scooter_logo).click()
#
#     def wait_navigation_base_page(self):
#         WebDriverWait(self.driver, 10).until(EC.url_contains('https://qa-scooter.praktikum-services.ru/'))
