from Locators import TensorPageLocators 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

class TensorPage: 
    def __init__(self,browser,url='https://tensor.ru/'): 
        self.browser = browser
        self.url = url
    def check_power_in_people(self): 
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(TensorPageLocators.LOCATOR_POWER_IN_PEOPLE)) 
            found = True 
        except:
            found = False 
        assert found, 'Error. Power of people element is not found'  
    def click_power_in_people_about(self): 
        power_in_people_about = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(TensorPageLocators.LOCATOR_POWER_IN_PEOPLE_ABOUT)) 
        expected_url = power_in_people_about.get_attribute('href') 
        power_in_people_about.click() 
        WebDriverWait(self.browser, 10).until(EC.url_to_be(expected_url)) 
    def check_tensor_about(self):
        page_url = self.browser.current_url 
        assert page_url == 'https://tensor.ru/about', 'Error. Page URL is not https://tensor.ru/about.' 
    def check_working_block(self): 
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(TensorPageLocators.LOCATOR_WORKING)) 
            found = True 
        except:
            found = False 
        assert found, 'Error. Working block is not found' 
    def check_size_of_working_images(self): 
        images = WebDriverWait(self.browser, 10).until(EC.visibility_of_all_elements_located(TensorPageLocators.LOCATOR_WORKING_IMAGES)) 
        size_of_picture = images[0].size 
        for image in images[1:]:
            assert image.size == size_of_picture, 'Error. Different dimensions of images' 
    
    
    
    
    
    
