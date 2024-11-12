from selenium.webdriver.common.by import By # импортировали из Selenium WebDriver модуль By для поиска элементов на веб-странице

class SbisPageLocators: # создали класс локаторов для страниц сайта sbis.ru
    LOCATOR_CONTACTS = (By.LINK_TEXT, "Контакты") # локатор для поиска раздела "Контакты"
    LOCATOR_TENSOR_BANNER = (By.XPATH, "//a[@href='https://tensor.ru/']") # локатор для поиска баннера Тензор. 
# ниже тестовый заведомо ошибочный локатор для проверки работоспособности теста
    # LOCATOR_TENSOR_BANNER = (By.XPATH, "//a[@href='https://faketensor.ru/']")
    LOCATOR_REGION = (By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']") # локатор для поиска региона в разделе Контакты
    LOCATOR_PARTNERS_LIST = (By.CLASS_NAME, 'sbisru-Contacts-List__col') # локатор для поиска блока со списком партнеров
# тестовый заведомо ошибочный локатор для проверки работоспособности теста
    # LOCATOR_PARTNERS_LIST = (By.CLASS_NAME, 'fakecontacts-ist__cy')
    LOCATOR_ELEMENT_OF_PARTNERS_LIST = (By.CLASS_NAME, 'sbisru-Contacts-List__col-1') # локатор для поиска хотя бы одного элемента в списке партнеров - проверяем, что он не пуст
# тестовый заведомо ошибочный локатор для проверки работоспособности теста
    # LOCATOR_ELEMENT_OF_PARTNERS_LIST = (By.CLASS_NAME, 'fakesbisru-Contacts-List__c1')
    LOCATOR_CHANGE_REGION = (By.CLASS_NAME, 'sbis_ru-link') # локатор для нахождения кнопки смены региона
    LOCATOR_OF_KAMCHATKA = (By.XPATH, "//ul[@class='sbis_ru-Region-Panel__list-l']//span[contains(@title,'Камчат')]") # локатор Камчатского края для смены региона
    LOCATOR_PARTNERS_LIST_REGION_TOWN = (By.CLASS_NAME, 'sbisru-Contacts-City__item-name') # локатор для проверки соответствия первого города в блоке со списком партнеров выбранному региону
    LOCATOR_DOWNLOAD = (By.CSS_SELECTOR, "[href='/download']") # локатор для поиска кнопки "Скачать локальные версии"
    LOCATOR_WEB_INSTALLER = (By.XPATH, "//a[contains(@href,'plugin-setup-web')]") # локатор для поиска ссылки для скачивания веб-установщика плагина СБИС

class TensorPageLocators:
    LOCATOR_POWER_IN_PEOPLE = (By.XPATH, "//p[text()='Сила в людях']") # локатор для поиска блока "Сила в людях"
# тестовый заведомо ошибочный локатор для проверки работоспособности теста
    # LOCATOR_POWER_IN_PEOPLE = (By.XPATH, "//p[text()='Сила в ньютонах']")
    LOCATOR_POWER_IN_PEOPLE_ABOUT = (By.XPATH, "//div[@class='tensor_ru-Index__block4-bg']//a[@href='/about']") # локатор для поиска кнопки "Подробнее" в блоке "Сила в людях"
    LOCATOR_WORKING = (By.XPATH, "//div[@class='tensor_ru-container tensor_ru-section tensor_ru-About__block3']//h2[text()='Работаем']") # локатор для поиска блока "Работаем"
# тестовый заведомо ошибочный локатор для проверки работоспособности теста
    # LOCATOR_WORKING = (By.XPATH, "//div[@class='tensor_ru-container tensor_ru-section tensor_ru-About__fakeblock3']//h2[text()='Работаем']")
    LOCATOR_WORKING_IMAGES = (By.XPATH, '//div[@class="tensor_ru-container tensor_ru-section tensor_ru-About__block3"]//img') # локатор для поиска изображений в блоке "Работаем"
