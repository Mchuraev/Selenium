from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    INVALID_ELEMENT = (By.CSS_SELECTOR, "#registration_link_invalid")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "[name=registration-email]")
    REGISTER_PASS_FIELD = (By.CSS_SELECTOR, "[name=registration-password1]")
    REGISTER_PASS_CONF_FIELD = (By.CSS_SELECTOR, "[name=registration-password2]")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")


class ProductPageLocators:
    BUTTON_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-lg')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div h1')
    PRODUCT_NAME_LAST = (By.CSS_SELECTOR, '.alertinner strong')
    PRODUCT_ADD_SUCCESS = (By.CSS_SELECTOR, '.alertinner')


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span .btn.btn-default:nth-child(1)")

class BasketPageLocators():
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p a")
    ADD_GOOD_IN_MAIN = (By.CSS_SELECTOR, ".col-xs-6:nth-child(1) button.btn")
    BASKET_NOT_EMPTY = (By.CSS_SELECTOR, "#basket_formset  div:nth-child(6)")
