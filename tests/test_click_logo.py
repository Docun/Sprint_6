from pages.logo_navigation import TestLogoNavigation
import allure


class TestYandexAndScootersLogo:
    @allure.title('Проверка лого "Яндекс"')
    @allure.description('Проверяем что по клику откроется страница Дзена')

    def test_yandex_logo(self, start_from_login_page):
        yandex_logo = TestLogoNavigation(start_from_login_page)
        yandex_logo.click_by_logo_yandex()
        yandex_logo.wait_for_navigation_to_dzen()

    @allure.title('Проверка лого "Самокат"')
    @allure.description('Проверяем что по клику по лого самоката перейдем обратно на глаавную')
    def test_scooter_logo(self, start_from_login_page):
        scooter_logo = TestLogoNavigation(start_from_login_page)
        scooter_logo.click_by_button_order()
        scooter_logo.click_by_logo_scooter()
        scooter_logo.check_url_base_page()




