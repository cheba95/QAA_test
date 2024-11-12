from SbisPages import SbisPage # подключили работу с объектами класса SbisPage из файла SbisPages.py

def test_sbis_search(browser):
    sbis_main_page = SbisPage(browser) # создали объект класса SbisPage для работы с помощью его методов
    sbis_main_page.go_to_sbis() # перешли на сайт https://sbis.ru
    sbis_main_page.click_contacts() # нажали на "Контакты"
    sbis_main_page.check_tensor_banner() # проверили, есть ли баннер "Тензор"
    tensor_main_page = sbis_main_page.click_tensor_banner() # нажали на баннер "Тензор", создали объект класса TensorPage для работы с помощью его методов
    tensor_main_page.check_power_in_people() # проверили, есть ли блок "Сила в людях"
    tensor_main_page.click_power_in_people_about() # нажали на "Подробнее" в блоке "Сила в людях"
    tensor_main_page.check_tensor_about() # проверили, открылась ли страница "https://tensor.ru/about"
    tensor_main_page.check_working_block() # проверили, есть ли раздел "Работаем"
    tensor_main_page.check_size_of_working_images() # проверили, что у всех фотографий в блоке "Работаем" одинаковая высота и ширина
