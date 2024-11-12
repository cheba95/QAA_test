from selenium.webdriver.support.ui import WebDriverWait # подключили модуль WebDriverWait для настройки ожиданий при загрузке веб-страниц и поиске элементов
from selenium.webdriver.support import expected_conditions as EC # подключили модуль expected_conditions для настройки ожиданий при загрузке веб-страниц и поиске элементов
from Locators import SbisPageLocators # подключили локаторы для страниц sbis.ru из файла Locators.py для их применения
from TensorPages import TensorPage # подключили класс TensorPage из файла TensorPages.py для его применения
import requests # модуль для скачивания файла
import os # модуль для определения, что файл скачан, и его размера.

class SbisPage: # создаем класс SbisPage
    def __init__(self,browser,url='https://sbis.ru/'): # при создании задаем атрибуты browser и url для работы через Selenium WebDriver с помощью pytest и conftest.py
        self.browser = browser 
        self.url = url
    def go_to_sbis(self): # метод перехода на сайт https://sbis.ru
        self.browser.get(self.url) 
    def click_contacts(self):  # метод перехода в раздел сайта "Контакты"
        contacts = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(SbisPageLocators.LOCATOR_CONTACTS)) # ждем до 10 секунд, пока элемент "Контакты" станет кликабельным, и назначаем переменную с элементом
        expected_url = contacts.get_attribute('href') # получаем URL ссылки по кнопке "Контакты"
        contacts.click() # нажимаем на кнопку "Контакты"
        WebDriverWait(self.browser, 10).until(EC.url_to_be(expected_url)) # ожидаем до 10 секунд, пока прогрузится страница
    def check_tensor_banner(self): # метод проверки наличия баннера "Тензор"
        try:
            WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(SbisPageLocators.LOCATOR_TENSOR_BANNER)) # проверяем наличие элемента с ожиданием до 10 секунд
            found = True # в случае успешного нахождения элемента - ставим флаг True, элемент найден
        except:
            found = False # если элемент не найден - ставим флаг False
        assert found, 'Error. Tensor banner is not found' # проверяем, найден ли объет, в случае, если не найден, в тесте возвращается указанный текст ошибки
    def click_tensor_banner(self): # метод нажатия на баннер "Тензор"
        tensor_banner = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(SbisPageLocators.LOCATOR_TENSOR_BANNER)) # ждем до 10 секунд, пока элемент"Тензор" станет кликабельным, и назначаем переменную с этим элементом
        expected_url = tensor_banner.get_attribute('href') # получаем URL ссылки по баннеру "Тензор"
        tensor_banner.click() # нажимаем на баннер
        self.browser.switch_to.window(self.browser.window_handles[-1]) # переключаемся на вкладку с сайтом tensor.ru для дальнейшей работы
        WebDriverWait(self.browser, 10).until(EC.url_to_be(expected_url)) # ожидаем до 10 секунд, пока прогрузится страница
        return TensorPage(browser=self.browser, url=self.browser.current_url) # возвращаем объект класса TensorPage для подключения в файле теста методов этого класса - работа с сайтом tensor.ru проводится с использованием файла TensorPages.py
    def check_region(self, name_of_region): # метод проверки региона на странице. При вызове метода нужно передать аргумент name_of_region, с которой будет проводиться сравнение информации о регионе с сайта
        region = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(SbisPageLocators.LOCATOR_REGION)) # ищем до 10 секунд элемент с регионом на сайте и присваиваем его переменной
        assert name_of_region in region.text, 'Error. Wrong region' # проверяем, соответствует ли регион на сайте региону, указанному в name_of_region
    def check_partners_list(self): # метод проверки наличия блока со списком партнеров 
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(SbisPageLocators.LOCATOR_PARTNERS_LIST)) # в течение до 10 секунд пробуем найти блок
            found = True # в случае успешного нахождения элемента - ставим флаг True, элемент найден
        except:
            found = False # если элемент не найден - ставим флаг False
        assert found, 'List of parters is not found'  # проверяем, найден ли объет, в случае, если не найден, в тесте возвращается указанный текст ошибки
    def check_partners_list_is_not_empty(self): # метод проверки, что блок не пустой и в нем есть хотя бы один элемент с адресом партнера
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(SbisPageLocators.LOCATOR_ELEMENT_OF_PARTNERS_LIST)) # в течение до 10 секунд пробуем найти блок
            found = True # в случае успешного нахождения элемента - ставим флаг True, элемент найден
        except:
            found = False # если элемент не найден - ставим флаг False
        assert found, 'List of parters has no elements' # проверяем, найден ли объет, в случае, если не найден, в тесте возвращается указанный текст ошибки
    def change_region(self): # метод нажатия на название региона с целью его смены
        change_region = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(SbisPageLocators.LOCATOR_CHANGE_REGION)) # в течение до 10 секунд пробуем найти элемент, если находим, присваиваем его переменной
        change_region.click() # нажимаем на кнопку, отображаем список регионов
    def choose_kamchatka(self): # метод выбора нужного региона - Камчатки
        kamchatka = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(SbisPageLocators.LOCATOR_OF_KAMCHATKA)) # в течение до 10 секунд пробуем найти элемент, если находим, присваиваем его переменной
        expected_url = 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients' # назначаем ожидаемый URL новой страницы для ожидания её прогрузки
        kamchatka.click() # нажимаем на Камчатский край
        WebDriverWait(self.browser, 10).until(EC.url_to_be(expected_url)) # ожидаем загрузки страницы
    def check_page_title(self, name_of_region): # метод проверки соответствия названия (заголовка) страницы в браузере указанному в аргументе name_of_region
        page_title = self.browser.title # назначаем переменную с заголовком текущей страницы
        assert name_of_region in page_title, 'Error. Wrong region by page title' # проверяем на соответствие заголовка текущей страницы заданному в name_of_region. В случае несоответствия в тесте возникает соответствующая ошибка
    def check_url(self, needed_url): # метод проверки соответствия URL текущей веб-страницы заданному в аргументе needed_url
        page_url = self.browser.current_url # присваиваем переменной URL текущей веб-страницы
        assert page_url.startswith(needed_url), 'Error. Wrong region by URL.' # проверяем на соответствие URL текущей страницы заданному в needed_url. В случае несоответствия в тесте возникает соответствующая ошибка
    def check_partners_list_region_town(self, name_of_town): # метод проверки соответствия первого города в списке партнеров заданному в аргументе name_of_town
        partners_list_region_town = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(SbisPageLocators.LOCATOR_PARTNERS_LIST_REGION_TOWN)) # в течение до 10 секунд пробуем найти элемент, если находим, присваиваем его переменной
        assert name_of_town in partners_list_region_town.text, 'Error. Wrong region by town.' # проверяем на соответствие первого города в списке партнеров на странице заданному в name_of_region. В случае несоответствия в тесте возникает соответствующая ошибка
    def check_download_local_versions(self): # метод проверки наличия кнопки "Скачать локальные версии"
        try:
            WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(SbisPageLocators.LOCATOR_DOWNLOAD)) # ищем элемент в течение до 10 секунд
            found = True # в случае успешного нахождения элемента - ставим флаг True, элемент найден
        except:
            found = False # если элемент не найден - ставим флаг False
        assert found, 'Download button is not found' # проверяем, найден ли объет, в случае, если не найден, в тесте возвращается указанный текст ошибки
    def click_download_local_versions(self): # метод нажатия на кнопку "Скачать локальные версии"
        download = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(SbisPageLocators.LOCATOR_DOWNLOAD)) # ищем ссылку на страницу со скачиванием версий в течение до 10 секунд, если находим - присваиваем переменной
        expected_url = download.get_attribute('href') # находим URL страницы с локальными версиями
        download.click() # нажимаем на кнопку "Скачать локальные версии"
        WebDriverWait(self.browser, 10).until(EC.url_to_be(expected_url)) # ждем загрузки страницы
    def download_web_installer(self): # метод скачивания веб-установщика
        download = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(SbisPageLocators.LOCATOR_WEB_INSTALLER)) # ищем в течение до 10 секунд кнопку скачивания веб-установщика
        link_url = download.get_attribute('href') # сохраняем в переменную ссылку для скачивания веб-установщика
        response = requests.get(link_url) # делаем запрос по ссылке и получаем ответ, сохраняем в переменную
        response.raise_for_status() # проверяем, понял ли сервер запрос 
        file_name = link_url[link_url.rfind('/') + 1:] # создаем переменную с названием файла. Название файла берем из конца ссылки на него
        with open(file_name, 'wb') as file: # записываем файл в папку с тестом
            file.write(response.content) 
        return download, file_name # возвращаем элемент с кнопкой скачивания и названием файла для последующих проверок
    def check_file_is_downloaded(self): # метод проверки того, что файл скачан
        file_name = self.download_web_installer()[1] # получаем из метода download_web_installer название файла и сохраняем в переменную
        assert os.path.isfile(file_name), 'Error. File does not exists' # проверяем наличие файла, иначе в тесте появляется ошибка с указанным текстом
    def check_size_of_file(self): # метод проверки соответствия размера скачанного файла размеру файла, указанному на сайте
        download, file_name = self.download_web_installer() # берем кнопку скачивания файла и имя файла из download_web_installer
        link_text = download.text # сохраняем в переменную текст кнопки с размером файла
        site_file_size = float("".join([i for i in link_text if i.isdigit() or i == "."])) # сохраняем в переменную размер файла, указанный на сайте
        real_file_size = round(os.path.getsize(file_name) / 1048576, 2) # сохраняем в переменную размер скачанного файла, делим на 1048576 для получения размера в МБ и округляем до 2 знаков после запятой
        assert site_file_size == real_file_size, 'Error. Size of downloaded file does not match size of file from site' # проверяем соответствие размера скачанного файла указанному на сайте.  В случае несоответствия в тесте возвращается указанный текст ошибки
