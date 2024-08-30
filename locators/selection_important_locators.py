from selenium.webdriver.common.by import By

class LocatorsSelection:
    
    # Все ВОПРОСЫ из блока "Вопросы о важном" с 1 по 7
    ALL_QUESTIONS = (By.ID, "accordion__heading-{}")

    # Все ОТВЕТЫ из блока "Вопросы о важном" с 1 по 7
    ALL_ANSWERS = (By.ID, "accordion__panel-{}")

    # Заголовок "Я живу за МКАДом, привезёте?"
    LIVE_FOR_MKAD = (By.ID, 'accordion__heading-7')






