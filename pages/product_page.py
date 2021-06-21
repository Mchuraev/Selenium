from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_busket = self.browser.find_element(*ProductPageLocators.BUTTON_TO_BASKET)
        add_busket.click()

    def cheack_name_goods(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def cheack_name_goods_last(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_LAST).text
