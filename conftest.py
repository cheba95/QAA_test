import pytest # подключаем Pytest
from selenium import webdriver # подключаем модуль webdriver из Selenium WebDriver для управления браузером через написанные автотесты

@pytest.fixture()
def browser():
    driver = webdriver.Chrome() # инициализируем браузер, создаем экземпляр Selenium WebDriver для браузера Chrome для тестов
    yield driver # разделитель в контексте автоматизации, все, что написано над ним, будет исполнено до теста, все, что ниже - после теста
    driver.quit() # закрываем браузер по завершении тестов