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

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADD_SUCCESS), \
            "Success message is presented, but should not be"

    def should_be_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADD_SUCCESS)
