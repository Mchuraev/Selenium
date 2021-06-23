from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.support import expected_conditions as EC


class BasketPage(BasePage):
    def should_be_message_empty(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY)

    def add_good(self):
        link = self.browser.find_element(*BasketPageLocators.ADD_GOOD_IN_MAIN)
        link.click()

    def should_be_not_empty(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_NOT_EMPTY)

    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY)

