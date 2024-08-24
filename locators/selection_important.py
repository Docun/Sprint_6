from selenium.webdriver.common.by import By

class LocatorsSelection:
    # Кнопка для кукис
    cookie_button = (By.CLASS_NAME, 'App_CookieButton__3cvqF')

    # Заголовок "Сколько это стоит? И как оплатить?"
    accordeon_huw_much = (By.ID, 'accordion__heading-0')

    # Открываемый контент из заголовка "Сколько это стоит? И как оплатить?"
    open_content_how_much = (By.ID, 'accordion__panel-0')

    # Заголовок "Хочу сразу несколько самокатов! Так можно?"
    accordion_some = (By.ID, 'accordion__heading-1')

    # Открываемый контент из заголовка "Пока что у нас так"
    open_content_some = (By.ID, 'accordion__panel-1')

    # Заголовок "Как рассчитывается время аренды?"
    accordion_rental = (By.ID, 'accordion__heading-2')

    # Открываемый контент из заголовка "Допустим, вы оформляете заказ на 8 мая"
    open_content_order = (By.ID, 'accordion__panel-2')

    # Заголовок "Можно ли заказать самокат прямо на сегодня?"
    accordion_rental_now = (By.ID, 'accordion__heading-3')

    # Открываемый контент из заголовка "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    open_content_order_more_quickly = (By.ID, 'accordion__panel-3')

    # Заголовок "Можно ли продлить заказ или вернуть самокат раньше?"
    accordion_return = (By.ID, 'accordion__heading-4')

    # Открываемый контент из заголовка "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    open_content_beautiful_number = (By.ID, 'accordion__panel-4')

    # Заголовок "Вы привозите зарядку вместе с самокатом?"
    accordion_charger = (By.ID, 'accordion__heading-5')

    # Открываемый контент из заголовка "Самокат приезжает к вам с полной зарядкой"
    open_content_full_energy = (By.ID, 'accordion__panel-5')

    # Заголовок "Можно ли отменить заказ?"
    accordion_cancel_order = (By.ID, 'accordion__heading-6')

    # Открываемый контент из заголовка "Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    open_content_no_penalty = (By.ID, 'accordion__panel-6')

    # Заголовок "Я живу за МКАДом, привезёте?"
    accordeon_live_for_mkad = (By.ID, 'accordion__heading-7')

    # Открываемый контент из заголовка "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    open_content_live_for_mkad = (By.ID, 'accordion__panel-7')




