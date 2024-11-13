from SbisPages import SbisPage 

def test_sbis_search(browser):
    sbis_main_page = SbisPage(browser) 
    sbis_main_page.go_to_sbis() 
    sbis_main_page.click_contacts() 
    sbis_main_page.check_tensor_banner() 
    tensor_main_page = sbis_main_page.click_tensor_banner() 
    tensor_main_page.check_power_in_people() 
    tensor_main_page.click_power_in_people_about() 
    tensor_main_page.check_tensor_about() 
    tensor_main_page.check_working_block() 
    tensor_main_page.check_size_of_working_images() 
