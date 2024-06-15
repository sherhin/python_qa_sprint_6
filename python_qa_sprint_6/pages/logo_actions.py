import allure

from pages.base_page import BasePage
from locators.base_locators import *


class LogoActions(BasePage):

    @allure.step('Переход по лого Яндекс')
    def click_on_yandex_logo(self):
        self.click_to_element(BasePageLocators.LOGO_SCOOTER)

    @allure.step('Переход по лого Самокат')
    def click_on_scooter_logo(self):
        self.click_to_element(BasePageLocators.LOGO_YANDEX)
        self.switch_tab(DzenLocators.DZEN_LOGO)