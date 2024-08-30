from selenium.webdriver.common.by import By

class MainPageLocators:

    # Кнопка Заказать в шапке
    ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')

    # Кнопка Заказать посередине страницы
    ORDER_BUTTON_TWO = (By.CSS_SELECTOR, ("#root > div > div > div.Header_Header__214zg > div.Header_Nav__AGCXC > button.Button_Button__ra12g"))

    # Кнопка для кукис
    COOKIE_BUTTONS = (By.CLASS_NAME, 'App_CookieButton__3cvqF')



