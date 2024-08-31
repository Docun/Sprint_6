from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.base_page_locators import MainPageLocators
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Проверяем, что текущий URL совпадает с ожидаемым')
    def verify_current_url(self, expected_url):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))
        current_url = self.driver.current_url
        return current_url == expected_url

    @allure.step('Вводим текст в поле')
    def entering_text_into_a_field(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    # @allure.step('Ищем текст о завершении заказа')
    # def get_element_text(self, locator, timeout=10):
    #     element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    #     return element.text
    #
    # @allure.step('Сравниваем текст с локатором')
    # def compare_element_text(self, locator, expected_text, timeout=10):
    #     actual_text = self.get_element_text(locator, timeout)
    #     return actual_text == expected_text

    def wait_for_number_of_windows(self, number_of_windows, url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(number_of_windows))
        windows = self.driver.window_handles
        new_window = [window for window in windows if window != self.driver.current_window_handle][0]
        self.driver.switch_to.window(new_window)
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url_part))
        current_url = self.driver.current_url
        if url_part not in current_url:
            raise AssertionError(f"Expected URL to contain '{url_part}', but got '{current_url}'")
        self.driver.close()
        original_window = [window for window in self.driver.window_handles if window != new_window][0]
        self.driver.switch_to.window(original_window)

    @allure.step('Скролим по странице до нужного элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Жмем на элемент')
    def click_button(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ждем что элемент будет виден на странице и в DOM')
    def wait_for_element_visibility(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # @allure.step('Ждем элемент и сохраняем в переменную')
    # def get_for_element(driver, locator, timeout=10):
    #     element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    #     return element

    @allure.step('Выключаем куки')
    def click_buttons_cockies(self):
        self.click_button(MainPageLocators.COOKIE_BUTTONS)




