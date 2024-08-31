from selenium.webdriver.common.by import By

class MainPageLocators:

    # Кнопка Заказать в шапке
    ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')

    # Кнопка Заказать в середине страницы
    BUTTON_MIDDLE = (By.XPATH, "//button[text()='Заказать']")

    # Кнопка для кукис
    COOKIE_BUTTONS = (By.CLASS_NAME, 'App_CookieButton__3cvqF')



