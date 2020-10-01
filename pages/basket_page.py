from .base_page import BasePage
from .locators import BasketPageLocators

#Создаём класс наследник. предок указывается в скобках.
class BasketPage(BasePage):
    def should_be_empty(self):
        self.should_not_be_product_in_basket()
        self.should_be_message_clear_basket()

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present (*BasketPageLocators.PRODUCT_IN_BASKET), "Product present in basket"

    def should_be_message_clear_basket(self):
        assert self.is_element_present (*BasketPageLocators.MESSAGE_CLEAR_BASKET), "Message 'clear basket' is not presented"
