from selenium.webdriver.common.by import By

class MainPageLocators:

    # Кнопка Заказать в шапке
    order_button = (By.CLASS_NAME, 'Button_Button__ra12g')

    # Кнопка Заказать посередине страницы
    order_button_two = (By.CSS_SELECTOR, ("#root > div > div > div.Header_Header__214zg > div.Header_Nav__AGCXC > button.Button_Button__ra12g"))

    # Кнопка для кукис
    cookie_button = (By.CLASS_NAME, 'App_CookieButton__3cvqF')



