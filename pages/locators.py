from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini > span .btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    FORM_REGISTER = (By.ID, "login_form")
    FORM_LOGIN = (By.ID, "register_form")
    EMAIL_FIELD = (By.ID, "id_registration-email")
    PASSWORD_FIELD = (By.ID, "id_registration-password1")
    PASSWORD_FIELD_REPEAD = (By.ID, "id_registration-password2")
    BUTTON_REGISTER = (By.NAME, "registration_submit")
    

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_PRODUCT =(By.CSS_SELECTOR, ".product_main h1")
    NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alertinner>strong")
    MESSAGE_TO_ADD = (By.CSS_SELECTOR, "#messages>div.alert")
    COST_BASKET = (By.CSS_SELECTOR, ".alert-info strong")
    COST_PRODUCT = (By.CSS_SELECTOR, "div.product_main .price_color")
    MESSAGE_COST = (By.CSS_SELECTOR, ".alert-info strong")

class BasketPageLocators():
    MESSAGE_CLEAR_BASKET = (By.CSS_SELECTOR, "div #content_inner > p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#content_inner > .basket_summary")