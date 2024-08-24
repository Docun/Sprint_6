from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Базовый класс, который будет содержать общие методы
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Метод для ожидания видимости элемента
    def wait_for_element_visibility(self, locator, timeout=3):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    # Метод для ожидания кликабельности элемента и выполнения клика
    def wait_and_click_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    # Метод для ожидания количества окон
    def wait_for_number_of_windows(self, number_of_windows, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(number_of_windows))

    # Метод для ожидания наличия URL
    def wait_for_url_contains(self, url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url_part))

    # Метод для ввода текста в поле
    def entering_text_into_a_field(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    # Метод для открытия url
    def open_url(self, url):
        self.driver.get(url)

    # Метод для скролла по странице до нужного элемента
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_text_from_field(self, locator):
        return self.driver.find_element(*locator).text

    def click_button(self, locator):
        self.driver.find_element(*locator).click()

    # Метод для проверки, содержит ли текущий URL ожидаемую подстроку
    def check_current_url_contains(self, expected_url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(expected_url_part))




