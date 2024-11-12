from SbisPages import SbisPage # подключили работу с объектами класса SbisPage из файла SbisPages.py

def test_sbis_search(browser):
    sbis_main_page = SbisPage(browser) # создали объект класса SbisPage для работы с помощью его методов
    sbis_main_page.go_to_sbis() # перешли на сайт https://sbis.ru
    sbis_main_page.click_contacts() # нажали на кнопку "Контакты"
    sbis_main_page.check_url('https://sbis.ru/contacts/66-sverdlovskaya-oblast') # проверили, что url страницы соответствует домашнему региону (в нашем случае - Свердловская область)
# тестовый заведомо ошибочный вариант для проверки работоспособности теста
    # sbis_main_page.check_url('https://sbis.ru/contacts/41-kamchatskij-kraj')
    sbis_main_page.check_page_title('Свердловск') # проверили, что title страницы в браузере соответствует домашнему региону
# тестовый заведомо ошибочный вариант для проверки работоспособности теста
    # sbis_main_page.check_page_title('Камчат')
    sbis_main_page.check_region('Свердловск') # проверили, что регион в блоке "Контакты" соответствует домашнему региону
# тестовый заведомо ошибочный вариант для проверки работоспособности теста
    # sbis_main_page.check_region('Камчат')
    sbis_main_page.check_partners_list() # проверили, есть ли список партнеров
    sbis_main_page.check_partners_list_region_town('Екатеринбург') # проверили, соответствует ли город в списке партнеров региону
# тестовый заведомо ошибочный вариант для проверки работоспособности теста
    # sbis_main_page.check_partners_list_region_town('Петропавловск-Камчатский')
    sbis_main_page.check_partners_list_is_not_empty() # проверили, не пуст ли список партнеров (ситуация когда блок с партнерами есть но пустой)
    sbis_main_page.change_region() # нажимаем на название региона для его смены
    sbis_main_page.choose_kamchatka() # нажимаем на Камчатский край
    sbis_main_page.check_url('https://sbis.ru/contacts/41-kamchatskij-kraj') # проверили, что url страницы соответствует Камчатскому краю
    sbis_main_page.check_page_title('Камчат') # проверили, что title страницы в браузере - Камчатский край
    sbis_main_page.check_region('Камчат') # проверили, что регион в блоке "Контакты" - Камчатский край
    sbis_main_page.check_partners_list() # проверили, есть ли список партнеров
    sbis_main_page.check_partners_list_region_town('Петропавловск-Камчатский') # проверили, соответствует ли город в списке партнеров региону
    sbis_main_page.check_partners_list_is_not_empty() # проверили, не пуст ли список партнеров 
