from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    FORM_REGISTER = (By.ID, "login_form")
    FORM_LOGIN = (By.ID, "register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_PRODUCT =(By.CSS_SELECTOR, ".product_main h1")
    NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alertinner>strong")
    MESSAGE_TO_ADD = (By.CSS_SELECTOR, "#messages>div.alert")
    COST_BASKET = (By.CSS_SELECTOR, ".alert-info strong")
    COST_PRODUCT = (By.CSS_SELECTOR, "div.product_main .price_color")
    MESSAGE_COST = (By.CSS_SELECTOR, ".alert-info strong")