from pages.product_page import ProductPage
import pytest
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.need_review
#Гость может добавить товар в корзину
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.should_be_add_product()
    page.should_be_message_add_to_basket()
    page.should_be_message_cost()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.should_be_add_product()
    page.should_not_be_success_message()

#Гость не видет сообщения о добавление товара при открытие страницы
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.should_be_add_product()
    page.element_should_disappear()

#Гость видит ссылку на Авторизацию
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
#Гость может перейти на страницу Авторизации со страницы продукта
def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
#Корзина гостя пустая если он не добавлял в неё товар
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()

@pytest.mark.user_add
#Тесты для зарегестрированого пользователя
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function",autouse=True)
    # Setup регистрация нового пользователя
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, login_link)
        login_page.open()
        email = str(time.time()) + "@dusya.official"
        password = "Qwerqwaz1"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user

    #Пользователь не видет сообщения о добавление товара при открытие страницы
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                         # открываем страницу
        page.should_not_be_success_message()

    @pytest.mark.need_review
    #Пользователь может добавить товар в корзину
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                         # открываем страницу
        page.should_be_add_product()
        page.should_be_message_add_to_basket()
        page.should_be_message_cost()