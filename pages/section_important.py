from locators.selection_important import LocatorsSelection
from BasePage import BasePage
from iniconf.curl import base_page
import allure

base_url = base_page


# 1. Класс для проверки раздела "Сколько стоит"
class CheckHowMuchSection(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.accordeon_huw_much = LocatorsSelection.accordeon_huw_much
        self.open_content_how_much = LocatorsSelection.open_content_how_much
        self.cookie_button = LocatorsSelection.cookie_button
        self.accordeon_live_for_mkad = LocatorsSelection.accordeon_live_for_mkad

    @allure.step('Проверяем что страница открылась')
    def wait_for_load_questions(self):
        self.wait_for_element_visibility(self.accordeon_huw_much)

    @allure.step('Скролим страницу до последнего раздела в конце страницы')
    def scroll_page_for_live(self):
        self.scroll_to_element(self.accordeon_live_for_mkad)

    @allure.step('Кликаем по кнопке куки')
    def click_cokies_now(self):
        self.click_button(self.cookie_button)

    @allure.step('кликаем по вопроссу сколько стоит')
    def click_questions(self):
        self.click_button(self.accordeon_huw_much)

    @allure.step('сравниваем текст из выпадающего меню')
    def examination_text(self):
        actual_text = self.driver.find_element(*self.open_content_how_much).text
        expected_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        assert expected_text in actual_text, f"Expected text '{expected_text}', but got '{actual_text}'"



# 2. Класс для проверки раздела "Хочу сразу несколько самокатов! Так можно?"
class CheckSomeScoters(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.accordeon_live_for_mkad = LocatorsSelection.accordeon_live_for_mkad
        self.open_content_some = LocatorsSelection.open_content_some
        self.accordion_some = LocatorsSelection.accordion_some
        self.cookie_button = LocatorsSelection.cookie_button

    @allure.step('Проверяем что страница открылась')
    def wait_for_load_questions(self):
        self.wait_for_element_visibility(self.accordion_some)

    @allure.step('Скролим страницу до последнего раздела в конце страницы')
    def scroll_page_for_live(self):
        self.scroll_to_element(self.accordeon_live_for_mkad)

    @allure.step('Кликаем по кнопке куки')
    def click_cockies_now(self):
        self.click_button(self.cookie_button)

    @allure.step('кликаем по вопросу "Хочу сразу несколько самокатов! Так можно?"')
    def click_questions(self):
        self.click_button(self.accordion_some)

    @allure.step('сравниваем текст из выпадающего меню')
    def examination_text(self):
        actual_text = self.driver.find_element(*self.open_content_some).text
        expected_text = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        assert expected_text in actual_text, f"Expected text '{expected_text}', but got '{actual_text}'"



# 3. Класс для проверки раздела "Как рассчитывается время аренды?"
class CheckResntalTime(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.accordeon_live_for_mkad = LocatorsSelection.accordeon_live_for_mkad
        self.accordion_rental = LocatorsSelection.accordion_rental
        self.open_content_order = LocatorsSelection.open_content_order
        self.cookie_button = LocatorsSelection.cookie_button

    @allure.step('Проверяем что страница открылась')
    def wait_for_load_questions(self):
        self.wait_for_element_visibility(self.accordion_rental)

    @allure.step('Скролим страницу до последнего раздела в конце страницы')
    def scroll_page_for_live(self):
        self.scroll_to_element(self.accordeon_live_for_mkad)

    @allure.step('Кликаем по кнопке куки')
    def click_cockies_now(self):
        self.click_button(self.cookie_button)

    @allure.step('кликаем по вопросу "Как рассчитывается время аренды?"')
    def click_questions(self):
        self.click_button(self.accordion_rental)

    @allure.step('сравниваем текст из выпадающего меню')
    def examination_text(self):
        actual_text = self.driver.find_element(*self.open_content_order).text
        expected_text = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        assert expected_text in actual_text, f"Expected text '{expected_text}', but got '{actual_text}'"



# 4. Класс для проверки раздела "Можно ли продлить заказ или вернуть самокат раньше?"
class CheckReturnOrder(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.accordeon_live_for_mkad = LocatorsSelection.accordeon_live_for_mkad
        self.accordion_return = LocatorsSelection.accordion_return
        self.open_content_beautiful_number = LocatorsSelection.open_content_beautiful_number
        self.cookie_button = LocatorsSelection.cookie_button

    @allure.step('Проверяем что страница открылась')
    def wait_for_load_questions(self):
        self.wait_for_element_visibility(self.accordion_return)

    @allure.step('Скролим страницу до последнего раздела в конце страницы')
    def scroll_page_for_live(self):
        self.scroll_to_element(self.accordeon_live_for_mkad)

    @allure.step('Кликаем по кнопке куки')
    def click_cockies_now(self):
        self.click_button(self.cookie_button)

    @allure.step('кликаем по вопросу "Можно ли продлить заказ или вернуть самокат раньше?"')
    def click_questions(self):
        self.click_button(self.accordion_return)

    @allure.step('сравниваем текст из выпадающего меню')
    def examination_text(self):
        actual_text = self.driver.find_element(*self.open_content_beautiful_number).text
        expected_text = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        assert expected_text in actual_text, f"Expected text '{expected_text}', but got '{actual_text}'"


# 5. Класс для проверки раздела "Вы привозите зарядку вместе с самокатом?"
class CheckQuickCharger(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.accordeon_live_for_mkad = LocatorsSelection.accordeon_live_for_mkad
        self.accordion_charger = LocatorsSelection.accordion_charger
        self.open_content_full_energy = LocatorsSelection.open_content_full_energy
        self.cookie_button = LocatorsSelection.cookie_button

    @allure.step('Проверяем что страница открылась')
    def wait_for_load_questions(self):
        self.wait_for_element_visibility(self.accordion_charger)

    @allure.step('Скролим страницу до последнего раздела в конце страницы')
    def scroll_page_for_live(self):
        self.scroll_to_element(self.accordeon_live_for_mkad)

    @allure.step('Кликаем по кнопке куки')
    def click_cockies_now(self):
        self.click_button(self.cookie_button)

    @allure.step('кликаем по вопросу "Вы привозите зарядку вместе с самокатом?"')
    def click_questions(self):
        self.click_button(self.accordion_charger)

    @allure.step('сравниваем текст из выпадающего меню')
    def examination_text(self):
        actual_text = self.driver.find_element(*self.open_content_full_energy).text
        expected_text = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        assert expected_text in actual_text, f"Expected text '{expected_text}', but got '{actual_text}'"





# 6. Класс для проверки раздела "Можно ли отменить заказ?"
class CheckCancelOrders(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.accordeon_live_for_mkad = LocatorsSelection.accordeon_live_for_mkad
        self.accordion_cancel_order = LocatorsSelection.accordion_cancel_order
        self.open_content_no_penalty = LocatorsSelection.open_content_no_penalty
        self.cookie_button = LocatorsSelection.cookie_button

    @allure.step('Проверяем что страница открылась')
    def wait_for_load_questions(self):
        self.wait_for_element_visibility(self.accordion_cancel_order)

    @allure.step('Скролим страницу до последнего раздела в конце страницы')
    def scroll_page_for_live(self):
        self.scroll_to_element(self.accordeon_live_for_mkad)

    @allure.step('Кликаем по кнопке куки')
    def click_cockies_now(self):
        self.click_button(self.cookie_button)

    @allure.step('кликаем по вопросу "Можно ли отменить заказ?"')
    def click_questions(self):
        self.click_button(self.accordion_cancel_order)

    @allure.step('сравниваем текст из выпадающего меню')
    def examination_text(self):
        actual_text = self.driver.find_element(*self.open_content_no_penalty).text
        expected_text = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        assert expected_text in actual_text, f"Expected text '{expected_text}', but got '{actual_text}'"


# 7. Класс для проверки раздела "Я живу за МКАДом, привезёте?"
class CheckLiveForMkad(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.accordeon_live_for_mkad = LocatorsSelection.accordeon_live_for_mkad
        self.open_content_live_for_mkad = LocatorsSelection.open_content_live_for_mkad
        self.cookie_button = LocatorsSelection.cookie_button

    @allure.step('Проверяем что страница открылась')
    def wait_for_load_questions(self):
        self.wait_for_element_visibility(self.accordeon_live_for_mkad)

    @allure.step('Скролим страницу до последнего раздела в конце страницы')
    def scroll_page_for_live(self):
        self.scroll_to_element(self.accordeon_live_for_mkad)

    @allure.step('Кликаем по кнопке куки')
    def click_cockies_now(self):
        self.click_button(self.cookie_button)

    @allure.step('кликаем по вопросу "Я живу за МКАДом, привезёте?"')
    def click_questions(self):
        self.click_button(self.accordeon_live_for_mkad)

    @allure.step('сравниваем текст из выпадающего меню')
    def examination_text(self):
        actual_text = self.driver.find_element(*self.open_content_live_for_mkad).text
        expected_text = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        assert expected_text in actual_text, f"Expected text '{expected_text}', but got '{actual_text}'"



# 8. Класс для проверки раздела "Можно ли заказать самокат прямо на сегодня?"
class CheckOrderToday(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.accordion_rental_now = LocatorsSelection.accordion_rental_now
        self.accordeon_live_for_mkad = LocatorsSelection.accordeon_live_for_mkad
        self.open_content_live_for_mkad = LocatorsSelection.open_content_order_more_quickly
        self.cookie_button = LocatorsSelection.cookie_button

    @allure.step('Проверяем что страница открылась')
    def wait_for_load_questions(self):
        self.wait_for_element_visibility(self.accordion_rental_now)

    @allure.step('Скролим страницу до последнего раздела в конце страницы')
    def scroll_page_for_live(self):
        self.scroll_to_element(self.accordeon_live_for_mkad)

    @allure.step('Кликаем по кнопке куки')
    def click_cockies_now(self):
        self.click_button(self.cookie_button)

    @allure.step('кликаем по вопросу "Можно ли заказать самокат прямо на сегодня?"')
    def click_questions(self):
        self.click_button(self.accordion_rental_now)

    @allure.step('сравниваем текст из выпадающего меню')
    def examination_text(self):
        actual_text = self.driver.find_element(*self.open_content_live_for_mkad).text
        expected_text = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        assert expected_text in actual_text, f"Expected text '{expected_text}', but got '{actual_text}'"



