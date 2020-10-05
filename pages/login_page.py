from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "Cant find word LOGIN in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.FORM_REGISTER), "Login register is not presented"

    def register_new_user(self, email, password):
        enter_email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        enter_email_field.send_keys(email)
        enter_password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        enter_password_field.send_keys(password)
        enter_password_repeat_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_REPEAD)
        enter_password_repeat_field.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        registration_button.click()
