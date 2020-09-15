
class BasePage():
    #Конструктор - метод. Передаём экземпляр драйвера и url адрес.
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    
    #Открываем нужную страницу в браузере
    def open(self):
        self.browser.get(self.url)