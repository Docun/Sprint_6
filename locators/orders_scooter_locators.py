from selenium.webdriver.common.by import By

class LocatorsOrder:

    # Кнопка Заказать посередине страницы
    ORDER_BUTTON_TWO = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")

    # Поле Имя
    FIELD_NAME = (By.XPATH, "//input[@placeholder='* Имя']")

    # Поле Фамилия
    FIELD_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")

    # Поле Адрес
    FIELD_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")

    # Поле Телефон
    FIELD_NUMBER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # Кнопка Дальше
    ORDER_NEXT = (By.XPATH, ".//button[contains(text(),'Далее')]")

    # Поле когда привезти самокат
    FIELD_BRING_ORDER = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    # давадцатое число в выпадающей панели
    DATE_TWENTY = (By.XPATH, '//*[text()="20"]')

    # Выпадающее поле срок аренды
    RENTAL_PERIOD = (By.CLASS_NAME, 'Dropdown-control')

    # Вариант Четверо суток из выпадающего меню
    FOUR_DAY = (By.XPATH, "//div[@class='Dropdown-option' and text()='четверо суток']")

    # Вариант Пятеро суток из выпадающего меню
    five_day = (By.XPATH, "//div[@class='Dropdown-option' and text()='пятеро суток']")

    # Чекбокс "серая безысходность"
    CHECKBOX_GRAY = (By.ID, 'grey')

    # Поле комент для курьера
    COMMENT_FOR_COURIER = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Кнопка ДА
    ORDERS_YES = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Да']")

    # Надпись статус заказа
    ORDERS_CHECK_STATUS = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and contains(text(), 'Заказ оформлен')]")

    # Надпись "Про аренду"
    INSCRIPTION = (By.CLASS_NAME, 'Order_Header__BZXOb')

    # Поле станция метро
    FIELD_STATION_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")

    # пункт из списка метро
    PARAGRAPH_METRO = (By.XPATH, '//*[text()="Бульвар Рокоссовского"]')










