from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    INVALID_ELEMENT = (By.CSS_SELECTOR, "#registration_link_invalid")