from SbisPages import SbisPage 

def test_sbis_search(browser):
    sbis_main_page = SbisPage(browser) 
    sbis_main_page.go_to_sbis() 
    sbis_main_page.check_download_local_versions() 
    sbis_main_page.click_download_local_versions() 
    sbis_main_page.download_web_installer() 
    sbis_main_page.check_file_is_downloaded() 
    sbis_main_page.check_size_of_file() 