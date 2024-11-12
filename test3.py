from SbisPages import SbisPage # подключили работу с объектами класса SbisPage из файла SbisPages.py

def test_sbis_search(browser):
    sbis_main_page = SbisPage(browser) # создали объект класса SbisPage для работы с помощью его методов
    sbis_main_page.go_to_sbis() # перешли на сайт https://sbis.ru
    sbis_main_page.check_download_local_versions() # проверили, что есть кнопка "Скачать локальные версии"
    sbis_main_page.click_download_local_versions() # нажали на кнопку "Скачать локальные версии"
    sbis_main_page.download_web_installer() # скачали веб-установщик
    sbis_main_page.check_file_is_downloaded() # проверили, что файл скачался
    sbis_main_page.check_size_of_file() # сравнили размер файла с размером, указанным на сайте