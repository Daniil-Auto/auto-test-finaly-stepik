from .base_page import BasePage
from .locators import ProductPageLocators
from .login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    #Добавляем продукт по кнопке
    def should_be_add_product(self):
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add.click()

    #Проверяем добален ли продукт и совпадает ли имя
    def should_be_message_add_to_basket(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_product_in_basket = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_BASKET).text
        assert self.is_element_present (*ProductPageLocators.MESSAGE_TO_ADD), "Message ADD is not presented"
        assert name_product == name_product_in_basket, "Product name does not match"

    #Проверяем есть ли сообщение о стоимости и верна ли сумма в корзине
    def should_be_message_cost(self):
        cost_product = self.browser.find_element(*ProductPageLocators.COST_PRODUCT).text
        cost_basket = self.browser.find_element(*ProductPageLocators.COST_BASKET).text
        assert self.is_element_present (*ProductPageLocators.MESSAGE_COST), "Message COST is not presented"
        assert cost_basket == cost_product, "Cart value is incorrect"
    
    #Проверочный код
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    #Проверяем что нет сообщения
    def should_not_be_success_message(self):
        assert self.is_not_element_present (*ProductPageLocators.MESSAGE_TO_ADD), "Message ADD is presented"

    #Проверяем что сообщение исчезло
    def element_should_disappear(self):
        assert self.is_disappeared (*ProductPageLocators.MESSAGE_TO_ADD), "Message ADD is disappeared"