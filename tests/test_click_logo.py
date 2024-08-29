from pages.base_click_logo import TestLogoNavigation
from iniconf.curl import base_page
class TestYandexAndScootersLogo:
    def test_logo_navigation(self, start_from_login_page):
        page = TestLogoNavigation(start_from_login_page)
        url = base_page
        page.open_new_page(url)
        page.wait_for_load_yandex_logo()
        page.click_by_logo_yandex()
        page.wait_for_navigation_to_dzen()
        page.close_and_open_new_page
        page.wait_for_load_scooter_logo()
        page.click_by_button_order()
        page.click_by_logo_scooter()
        page.wait_navigation_base_page()
        page.check_url_base_page()