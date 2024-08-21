from selenium.webdriver.common.by import By

class Locators_order:
    # Кнопка Заказать в шапке
    order_button = (By.CLASS_NAME, 'Button_Button__ra12g')

    # Кнопка Заказать по середине страницы
    order_button_two = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div[2]/div[5]/button')

    # Поле Имя
    field_name = (By.XPATH, "//input[@placeholder='* Имя']")

    # Поле Фамилия
    field_surname = (By.XPATH, "//input[@placeholder='* Фамилия']")

    # Поле Адрес
    field_address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")

    # Поле Телефон
    field_number = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # Кнопка Дальше
    order_next = (By.XPATH, ".//button[contains(text(),'Далее')]")

    # Поле когда привезти самокат
    field_bring_order = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    # давадцатое число в выпадающей панели
    date_twenty = (By.XPATH, '//*[text()="20"]')

    # тридцать первое число в выпадающей панели
    date_thirty = (By.XPATH, '//*[text()="31"]')

    # Выпадающее поле срок аренды
    rental_period = (By.CLASS_NAME, 'Dropdown-control')

    # Вариант Четверо суток из выпадающего меню
    four_day = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[4]')

    # Вариант Пятеро суток из выпадающего меню
    five_day = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[5]')

    # Чекбокс "чёрный жемчуг"
    checkbox_black = (By.CLASS_NAME, 'Checkbox_Input__14A2w')

    # Чекбокс "серая безысходность"
    checkbox_gray = (By.ID, 'grey')

    # Поле комент для курьера
    comment_for_courier = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Кнопка Заказать
    button_charter = (By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/button[2]')

    # Кнопка ДА
    order_yes = (By.XPATH, '//*[text()="Да"]')

    # Кнопка Посмотреть статус
    order_check_status = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')

    # Надпись "Про аренду"
    inscription = (By.CLASS_NAME, 'Order_Header__BZXOb')

    # Поле станция метро
    field_station_metro = (By.XPATH, "//input[@placeholder='* Станция метро']")

    # пункт из списка метро
    paragraph_metro = (By.XPATH, '//*[text()="Бульвар Рокоссовского"]')

    # пункт из списка метро
    paragraph_metro_two = (By.XPATH, '//*[text()="Охотный Ряд"]')










