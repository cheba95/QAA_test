from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import SbisPageLocators
from TensorPages import TensorPage
import requests
import os

class SbisPage:
    def __init__(self,browser,url='https://sbis.ru/'):
        self.browser = browser 
        self.url = url
    def go_to_sbis(self):
        self.browser.get(self.url) 
    def click_contacts(self):
        contacts = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(SbisPageLocators.LOCATOR_CONTACTS))
        expected_url = contacts.get_attribute('href')
        contacts.click()
        WebDriverWait(self.browser, 10).until(EC.url_to_be(expected_url))
    def check_tensor_banner(self):
        try:
            WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(SbisPageLocators.LOCATOR_TENSOR_BANNER))
            found = True
        except:
            found = False
        assert found, 'Error. Tensor banner is not found'
    def click_tensor_banner(self):
        tensor_banner = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(SbisPageLocators.LOCATOR_TENSOR_BANNER))
        expected_url = tensor_banner.get_attribute('href')
        tensor_banner.click()
        self.browser.switch_to.window(self.browser.window_handles[-1])
        WebDriverWait(self.browser, 10).until(EC.url_to_be(expected_url))
        return TensorPage(browser=self.browser, url=self.browser.current_url)
    def check_region(self, name_of_region):
        region = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(SbisPageLocators.LOCATOR_REGION))
        assert name_of_region in region.text, 'Error. Wrong region'
    def check_partners_list(self):
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(SbisPageLocators.LOCATOR_PARTNERS_LIST))
            found = True
        except:
            found = False
        assert found, 'Error. List of parters is not found'
    def check_partners_list_is_not_empty(self):
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(SbisPageLocators.LOCATOR_ELEMENT_OF_PARTNERS_LIST))
            found = True
        except:
            found = False
        assert found, 'Error. List of parters has no elements'
    def change_region(self): 
        change_region = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(SbisPageLocators.LOCATOR_CHANGE_REGION)) 
        change_region.click() 
    def choose_kamchatka(self): 
        kamchatka = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(SbisPageLocators.LOCATOR_OF_KAMCHATKA)) 
        expected_url = 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients' 
        kamchatka.click() 
        WebDriverWait(self.browser, 10).until(EC.url_to_be(expected_url)) 
    def check_page_title(self, name_of_region): 
        page_title = self.browser.title 
        assert name_of_region in page_title, 'Error. Wrong region by page title' 
    def check_url(self, needed_url): 
        page_url = self.browser.current_url 
        assert page_url.startswith(needed_url), 'Error. Wrong region by URL.' 
    def check_partners_list_region_town(self, name_of_town): 
        partners_list_region_town = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(SbisPageLocators.LOCATOR_PARTNERS_LIST_REGION_TOWN)) 
        assert name_of_town in partners_list_region_town.text, 'Error. Wrong region by town.' 
    def check_download_local_versions(self): 
        try:
            WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(SbisPageLocators.LOCATOR_DOWNLOAD)) 
            found = True 
        except:
            found = False 
        assert found, 'Error. Download button is not found' 
    def click_download_local_versions(self): 
        download = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(SbisPageLocators.LOCATOR_DOWNLOAD)) 
        expected_url = download.get_attribute('href') 
        download.click() 
        WebDriverWait(self.browser, 10).until(EC.url_to_be(expected_url)) 
    def download_web_installer(self): 
        download = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(SbisPageLocators.LOCATOR_WEB_INSTALLER)) 
        link_url = download.get_attribute('href') 
        response = requests.get(link_url) 
        response.raise_for_status() 
        file_name = link_url[link_url.rfind('/') + 1:] 
        with open(file_name, 'wb') as file: 
            file.write(response.content) 
        return download, file_name 
    def check_file_is_downloaded(self): 
        file_name = self.download_web_installer()[1] 
        assert os.path.isfile(file_name), 'Error. File does not exists' 
    def check_size_of_file(self): 
        download, file_name = self.download_web_installer() 
        link_text = download.text 
        site_file_size = float("".join([i for i in link_text if i.isdigit() or i == "."])) 
        real_file_size = round(os.path.getsize(file_name) / 1048576, 2) 
        assert site_file_size == real_file_size, 'Error. Size of downloaded file does not match size of file from site' 
