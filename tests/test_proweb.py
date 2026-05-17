import time
from time import sleep

from pages.auth_page import AuthPage
from pages.home_pages import HomePages
from pages.lessons_page import LessonsPage

def test_chrome(driver_chrome):
    driver_chrome.get("https://my.proweb.uz/log-in?q=/home")
    auth_page = AuthPage(driver_chrome)
    auth_page.enter_login("998941181463")
    time.sleep(2)
    auth_page.click_btn_login()
    time.sleep(2)
    auth_page.enter_password("proweb0211")
    time.sleep(2)
    auth_page.click_btn_submit()
    time.sleep(2)
    try:
        auth_page.click_btn_session()
        time.sleep(2)
        auth_page.click_btn_finish()
    except:
        pass

    home_pages= HomePages(driver_chrome)
    home_pages.click_video_instruction()
    time.sleep(2)
    home_pages.click_btn_fullscreen()
    time.sleep(10)
    home_pages.click_press_video()
    time.sleep(2)
    home_pages.click_btn_pause()
    time.sleep(2)
    home_pages.click_fullscreen_exit()
    time.sleep(2)
    home_pages.click_logo()
    time.sleep(2)
    home_pages.click_group_card()
    time.sleep(2)

    lessons_page = LessonsPage(driver_chrome)

    lessons_page.click_btn_lessons()
    time.sleep(2)
    lessons_page.click_lesson_card()
    time.sleep(2)
    lessons_page.click_btn_play_video()
    time.sleep(2)
    lessons_page.click_btn_fullscreen()
    time.sleep(10)
    lessons_page.click_press_video()
    time.sleep(2)
    lessons_page.click_btn_pause()
    time.sleep(2)
    lessons_page.click_fullscreen_exit()
    time.sleep(2)
    lessons_page.click_btn_back()
    time.sleep(2)

    home_pages.click_profile_icon()
    time.sleep(2)
    home_pages.click_btn_exit()
    time.sleep(2)
    home_pages.click_btn_confirm_exit()

