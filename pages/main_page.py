from .base_page import BasePage
from .locators import MainPageLocators

#Создаём класс наследник. предок указывается в скобках.
class MainPage(BasePage):
    #Заглушка т.к. все методы ушли в BasePage
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

