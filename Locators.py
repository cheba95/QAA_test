from selenium.webdriver.common.by import By 

class SbisPageLocators: 
    LOCATOR_CONTACTS = (By.LINK_TEXT, "Контакты")
    LOCATOR_TENSOR_BANNER = (By.XPATH, "//a[@href='https://tensor.ru/']")
    LOCATOR_REGION = (By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']") 
    LOCATOR_PARTNERS_LIST = (By.CLASS_NAME, 'sbisru-Contacts-List__col')
    LOCATOR_ELEMENT_OF_PARTNERS_LIST = (By.CLASS_NAME, 'sbisru-Contacts-List__col-1') 
    LOCATOR_CHANGE_REGION = (By.CLASS_NAME, 'sbis_ru-link') 
    LOCATOR_OF_KAMCHATKA = (By.XPATH, "//ul[@class='sbis_ru-Region-Panel__list-l']//span[contains(@title,'Камчат')]") 
    LOCATOR_PARTNERS_LIST_REGION_TOWN = (By.CLASS_NAME, 'sbisru-Contacts-City__item-name')
    LOCATOR_DOWNLOAD = (By.CSS_SELECTOR, "[href='/download']")
    LOCATOR_WEB_INSTALLER = (By.XPATH, "//a[contains(@href,'plugin-setup-web')]")

class TensorPageLocators:
    LOCATOR_POWER_IN_PEOPLE = (By.XPATH, "//p[text()='Сила в людях']")
    LOCATOR_POWER_IN_PEOPLE_ABOUT = (By.XPATH, "//div[@class='tensor_ru-Index__block4-bg']//a[@href='/about']")
    LOCATOR_WORKING = (By.XPATH, "//div[@class='tensor_ru-container tensor_ru-section tensor_ru-About__block3']//h2[text()='Работаем']")
    LOCATOR_WORKING_IMAGES = (By.XPATH, '//div[@class="tensor_ru-container tensor_ru-section tensor_ru-About__block3"]//img')
