from Locators import TensorPageLocators # подключили локаторы для страниц tensor.ru из файла Locators.py для их применения
from selenium.webdriver.support.ui import WebDriverWait # подключили модуль WebDriverWait для настройки ожиданий при загрузке веб-страниц и поиске элементов
from selenium.webdriver.support import expected_conditions as EC # подключили модуль expected_conditions для настройки ожиданий при загрузке веб-страниц и поиске элементов

class TensorPage: # создаем класс TensorPage
    def __init__(self,browser,url='https://tensor.ru/'): # при создании задаем атрибуты browser и url для работы через Selenium WebDriver с помощью pytest и conftest.py
        self.browser = browser
        self.url = url
    def check_power_in_people(self): # метод проверки наличия блока "Сила в людях"
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(TensorPageLocators.LOCATOR_POWER_IN_PEOPLE)) # ищем блок "Сила в людях" в течение 10 секунд
            found = True # в случае успешного нахождения элемента - ставим флаг True, элемент найден
        except:
            found = False # если элемент не найден - ставим флаг False
        assert found, 'Power of people element is not found'  # проверяем, найден ли объет, в случае, если не найден, в тесте возвращается указанный текст ошибки
    def click_power_in_people_about(self): # метод нажатия на кнопку "Подробнее" в блоке "Сила в людях"
        power_in_people_about = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(TensorPageLocators.LOCATOR_POWER_IN_PEOPLE_ABOUT)) # # ждем до 10 секунд, пока элемент "Подробнее" станет кликабельным, и назначаем переменную с этим элементом
        expected_url = power_in_people_about.get_attribute('href') # получаем URL ссылки по элементу "Подробнее"
        power_in_people_about.click() # нажимаем на "Подробнее"
        WebDriverWait(self.browser, 10).until(EC.url_to_be(expected_url)) # ожидаем до 10 секунд, пока прогрузится страница
    def check_tensor_about(self):
        page_url = self.browser.current_url # присваиваем переменной URL текущей веб-страницы
        assert page_url == 'https://tensor.ru/about', 'Error. Page URL is not https://tensor.ru/about.' # проверяем на соответствие URL требуемому. В случае несоответствия в тесте возникает соответствующая ошибка
    def check_working_block(self): # метод проверки, есть ли блок "Работаем"
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(TensorPageLocators.LOCATOR_WORKING)) # ищем блок "Работаем" в течение 10 секунд
            found = True # в случае успешного нахождения элемента - ставим флаг True, элемент найден
        except:
            found = False # если элемент не найден - ставим флаг False
        assert found, 'Working block is not found' # проверяем, найден ли объет, в случае, если не найден, в тесте возвращается указанный текст ошибки
    def check_size_of_working_images(self): # метод проверки, одинаковый ли размер фотографий в блоке
        images = WebDriverWait(self.browser, 10).until(EC.visibility_of_all_elements_located(TensorPageLocators.LOCATOR_WORKING_IMAGES)) # ищем фотографии в блоке "Работаем" и сохраняем в переменную
        size_of_picture = images[0].size # сохраняем в переменную размер первой фотографии
        for image in images[1:]:
            assert image.size == size_of_picture, 'Error. Different dimensions of images' # проверяем, соответствует ли размер остальных фотографий первой. Если нет - в тесте возвращается указанный текст ошибки
    # ниже тестовый заведомо ошибочный код для проверки работоспособности теста
    # def check_size_of_working_images(self): # метод проверки, 
    #     images = WebDriverWait(self.browser, 10).until(EC.visibility_of_all_elements_located(TensorPageLocators.LOCATOR_WORKING_IMAGES))
    #     size_of_picture = {'height': 191, 'width': 271}
    #     for image in images[1:]:
    #         assert image.size == size_of_picture, 'Error. Different dimensions of images'