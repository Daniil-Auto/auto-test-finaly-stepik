from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    FORM_REGISTER = (By.ID, "login_form")
    FORM_LOGIN = (By.ID, "register_form")