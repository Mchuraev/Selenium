from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    INVALID_ELEMENT = (By.CSS_SELECTOR, "#registration_link_invalid")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUTTON_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-lg')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div h1')
    PRODUCT_NAME_LAST = (By.CSS_SELECTOR, '.alertinner strong')