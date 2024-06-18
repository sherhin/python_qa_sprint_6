import allure
from data import *


@allure.story('Тесты переходов по логотипу Яндекс/Самокат')
class TestLogoActions:
    @allure.title('Тест перехода со страницы заказа на главную по клику на логотип "Самокат"')
    def test_logo_scooter(self, driver, logo_actions_from_order_page):
        logo_actions_from_order_page.open_page()
        logo_actions_from_order_page.click_on_yandex_logo()
        assert logo_actions_from_order_page.get_url() == Url.MAIN_PAGE

    @allure.title('Тест перехода со страницы заказа на страницу Яндекса по клику на логотип "Яндекс"')
    def test_logo_yandex(self, driver, logo_actions_from_order_page):
        logo_actions_from_order_page.open_page()
        logo_actions_from_order_page.click_on_scooter_logo()
        assert Url.DZEN_PAGE in logo_actions_from_order_page.get_url()