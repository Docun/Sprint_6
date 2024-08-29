from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Базовый класс, который будет содержать общие методы
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Метод для ожидания кликабельности элемента и выполнения клика
    def wait_and_click_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    # Метод для ожидания количества окон и сравнения url
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

    # Метод для ожидания наличия URL
    def wait_for_url_contains(self, url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url_part))


    # Метод для ввода текста в поле
    def entering_text_into_a_field(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    # Метод для скролла по странице до нужного элемента
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_button(self, locator):
        self.driver.find_element(*locator).click()

    def check_text(self, expected_url_part: str):
        current_url = self.driver.current_url
        assert expected_url_part in current_url, f"Expected '{expected_url_part}' to be part of '{current_url}'"

    def wait_for_element_visibility(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))


    def find_element_by_text_and_verify(self, locator, expected_text):
        element = self.driver.find_element(*locator)
        actual_text = element.text
        assert actual_text == expected_text, f'Expected text "{expected_text}" but got "{actual_text}".'


