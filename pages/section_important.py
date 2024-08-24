from locators.selection_important import LocatorsSelection
from test_base import BasePage


# 1. Класс для проверки раздела "Сколько стоит"
class CheckHowMuchSection(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.accordeon_huw_much = LocatorsSelection.accordeon_huw_much
        self.open_content_how_much = LocatorsSelection.open_content_how_much
        self.cookie_button = LocatorsSelection.cookie_button
        self.accordeon_live_for_mkad = LocatorsSelection.accordeon_live_for_mkad

    def wait_for_load_questions(self):
        self.driver.wait_for_element_visibility(self.accordeon_huw_much)

    def scroll_page_for_live(self):
        self.driver.scroll_to_element(self.accordeon_live_for_mkad)

    def click_cokies_now(self):
        self.driver.click_button(self.cookie_button)

    def click_questions(self):
        self.driver.click_button(self.accordeon_huw_much)

    def get_text_section_how_much(self):
        self.driver.get_text_from_field(self.open_content_how_much)
# class HowMuchSection:
#     def __init__(self, driver):
#         self.driver = driver
#         self.accordeon_huw_much = LocatorsSelection.accordeon_huw_much
#         self.open_content_how_much = LocatorsSelection.open_content_how_much
#         self.cookie_button = LocatorsSelection.cookie_button
#         self.accordeon_live_for_mkad = LocatorsSelection.accordeon_live_for_mkad
#
#     # метод ожидания загрузки страницы
#     def wait_for_load_how_much(self):
#         WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.accordeon_huw_much))
#
#     # метод для прокрутки страницы до нужного элемента
#     def scroll_page_for_live(self):
#         element = self.driver.find_element(*self.accordeon_live_for_mkad)
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
#         element.send_keys(self.accordeon_live_for_mkad)
#
#     # метод для клика по кнопке с куки
#     def click_cokies_now(self):
#         self.driver.find_element(*self.cookie_button).click()
#
#     # метод для клика по разделу "Сколько стоит?"
#     def click_how_much(self):
#         self.driver.find_element(*self.accordeon_huw_much).click()
#
#     # метод для получения текста раздела "Сколько стоит?"
#     def get_text_section_how_much(self):
#         return self.driver.find_element(*self.open_content_how_much).text



# 2. Класс для проверки раздела "Хочу сразу несколько самокатов! Так можно?"
class CheckSomeScoters(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.accordeon_live_for_mkad = LocatorsSelection.accordeon_live_for_mkad
        self.open_content_some = LocatorsSelection.open_content_some
        self.accordion_some = LocatorsSelection.accordion_some
        self.cookie_button = LocatorsSelection.cookie_button
    def wait_for_load_questions(self):
        self.driver.wait_for_element_visibility(self.accordion_some)

    def scroll_page_for_live(self):
        self.driver.scroll_to_element(self.accordeon_live_for_mkad)

    def click_cockies_now(self):
        self.driver.click_button(self.cookie_button)

    def click_questions(self):
        self.driver.click_button(self.accordion_some)

    def get_text_section_scoters(self):
        self.driver.get_text_from_field(self.open_content_some)
# class SomeScooters:
#     def __init__(self, driver):
#         self.accordeon_live_for_mkad = LocatorsSelection.accordeon_live_for_mkad
#         self.open_content_some = LocatorsSelection.open_content_some
#         self.accordion_some = LocatorsSelection.accordion_some
#         self.cookie_button = LocatorsSelection.cookie_button
#         self.driver = driver
#
#     # метод ожидания загрузки страницы
#     def wait_for_load_scoters(self):
#         WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.accordion_some))
#
#     # метод для прокрутки страницы до нужного элемента
#     def scroll_page_for_live(self):
#         element = self.driver.find_element(*self.accordeon_live_for_mkad)
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
#         element.send_keys(self.accordeon_live_for_mkad)
#
#     # метод для клика по кнопке с куки
#     def click_cokies_now(self):
#         self.driver.find_element(*self.cookie_button).click()
#
#     # метод для клика по разделу "Хочу сразу несколько самокатов! Так можно?"
#     def click_some_scoters(self):
#         self.driver.find_element(*self.accordion_some).click()
#
#     # метод для получения текста раздела "Хочу сразу несколько самокатов! Так можно?"
#     def get_text_section_scoters(self):
#         return self.driver.find_element(*self.open_content_some).text



# 3. Класс для проверки раздела "Как рассчитывается время аренды?"
class CheckResntalTime(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.accordeon_live_for_mkad = LocatorsSelection.accordeon_live_for_mkad
        self.accordion_rental = LocatorsSelection.accordion_rental
        self.open_content_order = LocatorsSelection.open_content_order
        self.cookie_button = LocatorsSelection.cookie_button

    def wait_for_load_questions(self):
        self.driver.wait_for_element_visibility(self.accordion_rental)

    def scroll_page_for_live(self):
        self.driver.scroll_to_element(self.accordeon_live_for_mkad)

    def click_cockies_now(self):
        self.driver.click_button(self.cookie_button)

    def click_questions(self):
        self.driver.click_button(self.accordion_rental)

    def get_text_section_scoters(self):
        self.driver.get_text_from_field(self.open_content_order)
# class RentalTime:
#     def __init__(self, driver):
#         self.accordeon_live_for_mkad = Locators_selection.accordeon_live_for_mkad
#         self.accordion_rental = Locators_selection.accordion_rental
#         self.open_content_order = Locators_selection.open_content_order
#         self.cookie_button = Locators_selection.cookie_button
#         self.driver = driver
#
#     # метод ожидания загрузки страницы
#     def wait_for_load_orders(self):
#         WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.accordion_rental))
#
#     # метод для прокрутки страницы до нужного элемента
#     def scroll_page_for_live(self):
#         element = self.driver.find_element(*self.accordeon_live_for_mkad)
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
#         element.send_keys(self.accordeon_live_for_mkad)
#
#     # метод для клика по кнопке с куки
#     def click_cokies_now(self):
#         self.driver.find_element(*self.cookie_button).click()
#
#     # метод для клика по разделу "Как рассчитывается время аренды?"
#     def click_some_time_order(self):
#         self.driver.find_element(*self.accordion_rental).click()
#
#     # метод для получения текста раздела "Допустим, вы оформляете заказ на 8 мая"
#     def get_text_section_order(self):
#         return self.driver.find_element(*self.open_content_order).text


# 4. Класс для проверки раздела "Можно ли продлить заказ или вернуть самокат раньше?"
class CheckReturnOrder(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.accordeon_live_for_mkad = LocatorsSelection.accordeon_live_for_mkad
        self.accordion_return = LocatorsSelection.accordion_return
        self.open_content_beautiful_number = LocatorsSelection.open_content_beautiful_number
        self.cookie_button = LocatorsSelection.cookie_button

    def wait_for_load_questions(self):
        self.driver.wait_for_element_visibility(self.accordion_return)

    def scroll_page_for_live(self):
        self.driver.scroll_to_element(self.accordeon_live_for_mkad)

    def click_cockies_now(self):
        self.driver.click_button(self.cookie_button)

    def click_questions(self):
        self.driver.click_button(self.accordion_return)

    def get_text_section_scoters(self):
        self.driver.get_text_from_field(self.open_content_beautiful_number)


# class ReturnOrder:
#     def __init__(self, driver):
#         self.accordeon_live_for_mkad = Locators_selection.accordeon_live_for_mkad
#         self.accordion_return = Locators_selection.accordion_return
#         self.open_content_beautiful_number = Locators_selection.open_content_beautiful_number
#         self.cookie_button = Locators_selection.cookie_button
#         self.driver = driver
#
#     # метод ожидания загрузки страницы
#     def wait_for_load_orders(self):
#         WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.accordion_return))
#
#     # метод для прокрутки страницы до нужного элемента
#     def scroll_page_for_live(self):
#         element = self.driver.find_element(*self.accordeon_live_for_mkad)
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
#         element.send_keys(self.accordeon_live_for_mkad)
#
#     # метод для клика по кнопке с куки
#     def click_cokies_now(self):
#         self.driver.find_element(*self.cookie_button).click()
#
#     # метод для клика по разделу "Можно ли продлить заказ или вернуть самокат раньше?"
#     def click_some_return_order(self):
#         self.driver.find_element(*self.accordion_return).click()
#
#     # метод для получения текста раздела "позвонить в поддержку по красивому номеру"
#     def get_text_section_order(self):
#         return self.driver.find_element(*self.open_content_beautiful_number).text






# 5. Класс для проверки раздела "Вы привозите зарядку вместе с самокатом?"
class CheckQuickCharger(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.accordeon_live_for_mkad = LocatorsSelection.accordeon_live_for_mkad
        self.accordion_charger = LocatorsSelection.accordion_charger
        self.open_content_full_energy = LocatorsSelection.open_content_full_energy
        self.cookie_button = LocatorsSelection.cookie_button

    def wait_for_load_questions(self):
        self.driver.wait_for_element_visibility(self.accordion_charger)

    def scroll_page_for_live(self):
        self.driver.scroll_to_element(self.accordeon_live_for_mkad)

    def click_cockies_now(self):
        self.driver.click_button(self.cookie_button)

    def click_questions(self):
        self.driver.click_button(self.accordion_charger)

    def get_text_section_scoters(self):
        self.driver.get_text_from_field(self.open_content_full_energy)
# class QuickCharger:
#     def __init__(self, driver):
#         self.accordeon_live_for_mkad = Locators_selection.accordeon_live_for_mkad
#         self.accordion_charger = Locators_selection.accordion_charger
#         self.open_content_full_energy = Locators_selection.open_content_full_energy
#         self.cookie_button = Locators_selection.cookie_button
#         self.driver = driver
#
#     # метод ожидания загрузки страницы
#     def wait_for_load_orders(self):
#         WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.accordion_charger))
#
#     # метод для прокрутки страницы до нужного элемента
    # def scroll_page_for_live(self):
    #     element = self.driver.find_element(*self.accordeon_live_for_mkad)
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    #     element.send_keys(self.accordeon_live_for_mkad)
    #
    # # метод для клика по кнопке с куки
    # def click_cokies_now(self):
    #     self.driver.find_element(*self.cookie_button).click()
    #
    # # метод для клика по разделу "Вы привозите зарядку вместе с самокатом?"
    # def click_some_time_order(self):
    #     self.driver.find_element(*self.accordion_charger).click()
    #
    # # метод для получения текста раздела "Самокат приезжает к вам с полной зарядкой"
    # def get_text_section_order(self):
    #     return self.driver.find_element(*self.open_content_full_energy).text





# 6. Класс для проверки раздела "Можно ли отменить заказ?"
class CheckCancelOrders(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.accordeon_live_for_mkad = LocatorsSelection.accordeon_live_for_mkad
        self.accordion_cancel_order = LocatorsSelection.accordion_cancel_order
        self.open_content_no_penalty = LocatorsSelection.open_content_no_penalty
        self.cookie_button = LocatorsSelection.cookie_button

    def wait_for_load_questions(self):
        self.driver.wait_for_element_visibility(self.accordion_cancel_order)

    def scroll_page_for_live(self):
        self.driver.scroll_to_element(self.accordeon_live_for_mkad)

    def click_cockies_now(self):
        self.driver.click_button(self.cookie_button)

    def click_questions(self):
        self.driver.click_button(self.accordion_cancel_order)

    def get_text_section_scoters(self):
        self.driver.get_text_from_field(self.open_content_no_penalty)
# class CancelOrders:
#     def __init__(self, driver):
#         self.accordeon_live_for_mkad = Locators_selection.accordeon_live_for_mkad
#         self.accordion_cancel_order = Locators_selection.accordion_cancel_order
#         self.open_content_no_penalty = Locators_selection.open_content_no_penalty
#         self.cookie_button = Locators_selection.cookie_button
#         self.driver = driver
#
#     # метод ожидания загрузки страницы
#     def wait_for_load_orders(self):
#         WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.accordion_cancel_order))
#
#     # метод для прокрутки страницы до нужного элемента
#     def scroll_page_for_live(self):
#         element = self.driver.find_element(*self.accordeon_live_for_mkad)
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
#         element.send_keys(self.accordeon_live_for_mkad)
#
#     # метод для клика по кнопке с куки
#     def click_cokies_now(self):
#         self.driver.find_element(*self.cookie_button).click()
#
#     # метод для клика по разделу "Можно ли отменить заказ?"
#     def click_some_time_order(self):
#         self.driver.find_element(*self.accordion_cancel_order).click()
#
#     # метод для получения текста раздела "Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
#     def get_text_section_order(self):
#         return self.driver.find_element(*self.open_content_no_penalty).text




# 7. Класс для проверки раздела "Я живу за МКАДом, привезёте?"
class CheckLiveForMkad(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.accordeon_live_for_mkad = LocatorsSelection.accordeon_live_for_mkad
        self.open_content_live_for_mkad = LocatorsSelection.open_content_live_for_mkad
        self.cookie_button = LocatorsSelection.cookie_button

    def wait_for_load_orders(self):
        self.driver.wait_for_element_visibility(self.accordeon_live_for_mkad)

    def scroll_page_for_live(self):
        self.driver.scroll_to_element(self.accordeon_live_for_mkad)

    def click_cockies_now(self):
        self.driver.click_button(self.cookie_button)

    def click_questions(self):
        self.driver.click_button(self.accordeon_live_for_mkad)

    def get_text_section_scoters(self):
        self.driver.get_text_from_field(self.open_content_live_for_mkad)
# class LiveForMkad:
#     def __init__(self, driver):
#         self.accordeon_live_for_mkad = Locators_selection.accordeon_live_for_mkad
#         self.open_content_live_for_mkad = Locators_selection.open_content_live_for_mkad
#         self.cookie_button = Locators_selection.cookie_button
#         self.driver = driver
#
#     # метод ожидания загрузки страницы
#     def wait_for_load_orders(self):
#         WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.accordeon_live_for_mkad))
#
#     # метод для прокрутки страницы до нужного элемента
#     def scroll_page_for_live(self):
#         element = self.driver.find_element(*self.accordeon_live_for_mkad)
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
#         element.send_keys(self.accordeon_live_for_mkad)
#
#     # метод для клика по кнопке с куки
#     def click_cokies_now(self):
#         self.driver.find_element(*self.cookie_button).click()
#
#     # метод для клика по разделу "Я живу за МКАДом, привезёте?"
#     def click_section_live_mkad(self):
#         self.driver.find_element(*self.accordeon_live_for_mkad).click()
#
#     # метод для получения текста раздела "Да, обязательно. Всем самокатов! И Москве, и Московской области."
#     def get_text_section_live_mkad(self):
#         return self.driver.find_element(*self.open_content_live_for_mkad).text

