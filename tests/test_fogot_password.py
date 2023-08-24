import pytest
from pages.main_page import MainPage
from setting import *


# ТС RT 007 Ссылка Забыли пароль работает
def test_fogot_pass(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.LINK_FOGOT_PASS)
    fog_passw = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert fog_passw == BaseUrl.FOG_PASSWORD
