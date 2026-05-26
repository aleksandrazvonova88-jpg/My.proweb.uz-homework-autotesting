import time
from time import sleep

from pages.auth_page import AuthPage
from pages.home_pages import HomePages
from pages.lessons_page import LessonsPage
from pages.coworking_page import CoworkingPage
from pages.homework_page import HomeworkPage

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

    # lessons_page = LessonsPage(driver_chrome)
    #
    # lessons_page.click_btn_lessons()
    # time.sleep(2)
    # lessons_page.click_lesson_card()
    # time.sleep(2)
    # lessons_page.click_btn_play_video()
    # time.sleep(2)
    # lessons_page.click_btn_fullscreen()
    # time.sleep(10)
    # lessons_page.click_press_video()
    # time.sleep(2)
    # lessons_page.click_btn_pause()
    # time.sleep(2)
    # lessons_page.click_fullscreen_exit()
    # time.sleep(2)
    #
    # try:
    #     lessons_page.click_rating()
    #     time.sleep(2)
    #
    #     lessons_page.click_send_rating()
    #     time.sleep(2)
    #
    # except Exception as e:
    #     print(f"Рейтинг не удалось отправить: {e}")
    #
    # # lessons_page.click_rating()
    # # time.sleep(2)
    # # lessons_page.click_send_rating()
    # # time.sleep(2)
    # lessons_page.click_btn_back()
    # time.sleep(2)

    homework_page = HomeworkPage(driver_chrome)
    homework_page.click_homeworks()
    homework_page.click_homework_dd()
    homework_page.click_go_to_homework()

    homework_page.click_comment_input()
    homework_page.enter_comment_input("1")
    homework_page.click_send_comment()

    home_pages.click_coworking_section()
    time.sleep(2)

    coworking_page = CoworkingPage(driver_chrome)
    coworking_page.click_btn_cw_sign_up()
    time.sleep(2)
    coworking_page.click_chb_filial()
    time.sleep(2)
    coworking_page.click_chb_room()
    time.sleep(2)

    coworking_page.click_btn_select()
    time.sleep(2)

    coworking_page.click_btn_date()
    time.sleep(2)

    coworking_page.click_group_choose()
    time.sleep(2)

    coworking_page.click_chb_select_group()
    time.sleep(2)

    coworking_page.click_btn_select_group()
    time.sleep(2)

    coworking_page.click_time_choose()
    time.sleep(2)

    coworking_page.click_btn_time_choose()
    time.sleep(2)

    coworking_page.click_place_choose()
    time.sleep(2)

    coworking_page.click_chb_place()
    time.sleep(2)

    coworking_page.click_btn_place_choose()
    time.sleep(2)

    coworking_page.click_btn_send()
    time.sleep(2)

    coworking_page.click_btn_cancel()
    time.sleep(2)

    coworking_page.click_btn_confirm_cancel()
    time.sleep(2)

    home_pages.click_profile_icon()
    time.sleep(2)
    home_pages.click_btn_exit()
    time.sleep(2)
    home_pages.click_btn_confirm_exit()



def test_invalid_auth_chrome(driver_chrome):
    driver_chrome.get('https://my.proweb.uz/log-in?q=/home')
    auth_page = AuthPage(driver_chrome)
    auth_page.click_btn_uz()
    time.sleep(2)
    auth_page.enter_login('998941181463')
    time.sleep(2)
    auth_page.click_btn_login()
    time.sleep(2)
    auth_page.enter_password('prowebproweb')
    time.sleep(2)
    auth_page.click_btn_submit()
    try:
        auth_page.click_btn_session()
        time.sleep(2)
        auth_page.click_btn_finish()
    except:
        pass

def test_auth_edge(driver_edge):
    driver_edge.get('https://my.proweb.uz/log-in?q=/home')
    auth_page = AuthPage(driver_edge)
    auth_page.click_btn_uz()
    time.sleep(2)
    auth_page.enter_login('998941181463')
    time.sleep(2)
    auth_page.click_btn_login()
    time.sleep(2)
    auth_page.enter_password('proweb0211')
    time.sleep(2)
    auth_page.click_btn_submit()
    try:
        auth_page.click_btn_session_edge()
        time.sleep(2)
        auth_page.click_btn_finish_edge()
    except:
        pass

    home_page = HomePages(driver_edge)
    home_page.click_video_instruction()
    time.sleep(2)
    home_page.click_btn_fullscreen()
    time.sleep(10)
    home_page.click_press_video()
    time.sleep(2)
    home_page.click_btn_pause()
    time.sleep(2)
    home_page.click_fullscreen_exit()
    time.sleep(2)
    home_page.click_logo()
    time.sleep(2)
    home_page.click_group_card()
    time.sleep(2)

    lessons_page = LessonsPage(driver_edge)
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

    try:
        lessons_page.click_rating()
        time.sleep(2)

        lessons_page.click_send_rating()
        time.sleep(2)

    except Exception as e:
        print(f"Рейтинг не удалось отправить: {e}")

    # lessons_page.click_rating()
    # time.sleep(2)
    # lessons_page.click_send_rating()
    # time.sleep(2)
    lessons_page.click_btn_back()
    time.sleep(2)

    homework_page = HomeworkPage(driver_edge)
    homework_page.click_homeworks()
    homework_page.click_homework_dd()
    homework_page.click_go_to_homework()

    homework_page.click_comment_input()
    homework_page.enter_comment_input("1")
    homework_page.click_send_comment()

    home_page.click_coworking_section()
    time.sleep(2)

    coworking_page = CoworkingPage(driver_edge)
    coworking_page.click_btn_cw_sign_up()
    time.sleep(2)
    coworking_page.click_chb_filial()
    time.sleep(2)
    coworking_page.click_chb_room()
    time.sleep(2)

    coworking_page.click_btn_select()
    time.sleep(2)

    coworking_page.click_btn_date()
    time.sleep(2)

    coworking_page.click_group_choose()
    time.sleep(2)

    coworking_page.click_chb_select_group()
    time.sleep(2)

    coworking_page.click_btn_select_group()
    time.sleep(2)

    coworking_page.click_time_choose()
    time.sleep(2)

    coworking_page.click_btn_time_choose()
    time.sleep(2)

    coworking_page.click_place_choose()
    time.sleep(2)

    coworking_page.click_chb_place()
    time.sleep(2)

    coworking_page.click_btn_place_choose()
    time.sleep(2)

    coworking_page.click_btn_send()
    time.sleep(2)

    coworking_page.click_btn_cancel()
    time.sleep(2)

    coworking_page.click_btn_confirm_cancel()
    time.sleep(2)

    home_page.click_profile_icon()
    time.sleep(2)
    home_page.click_btn_exit()
    time.sleep(2)
    home_page.click_btn_confirm_exit()

def test_auth_Firefox(driver_firefox):
    driver_firefox.get('https://my.proweb.uz/log-in?q=/home')
    auth_page = AuthPage(driver_firefox)
    auth_page.click_btn_uz()
    time.sleep(2)
    auth_page.enter_login('998941181463')
    time.sleep(2)
    auth_page.click_btn_login()
    time.sleep(2)
    auth_page.enter_password_ff('proweb0211')
    time.sleep(2)
    auth_page.click_btn_submit()
    time.sleep(5)
    try:
        auth_page.click_btn_session_ff()
        time.sleep(2)
        auth_page.click_btn_finish_ff()
    except:
        pass

    home_page = HomePages(driver_firefox)
    home_page.click_video_instruction()
    time.sleep(2)
    home_page.click_btn_fullscreen_ff()
    time.sleep(10)
    home_page.click_press_video()
    time.sleep(2)
    home_page.click_btn_pause()
    time.sleep(2)
    home_page.click_fullscreen_exit_ff()
    time.sleep(2)
    home_page.click_logo()
    time.sleep(2)
    home_page.click_group_card()
    time.sleep(2)

    lessons_page = LessonsPage(driver_firefox)
    lessons_page.click_btn_lessons()
    time.sleep(2)
    lessons_page.click_lesson_card()
    time.sleep(2)
    lessons_page.click_btn_play_video()
    time.sleep(2)
    lessons_page.click_btn_fullscreen_ff()
    time.sleep(10)
    lessons_page.click_press_video()
    time.sleep(2)
    lessons_page.click_btn_pause()
    time.sleep(2)
    lessons_page.click_fullscreen_exit_ff()
    time.sleep(2)

    try:
        lessons_page.click_rating()
        time.sleep(2)

        lessons_page.click_send_rating()
        time.sleep(2)

    except Exception as e:
        print(f"Рейтинг не удалось отправить: {e}")

    # lessons_page.click_rating()
    # time.sleep(2)
    # lessons_page.click_send_rating()
    # time.sleep(2)
    lessons_page.click_btn_back()
    time.sleep(2)

    homework_page = HomeworkPage(driver_firefox)
    homework_page.click_homeworks()
    homework_page.click_homework_dd()
    homework_page.click_go_to_homework()

    homework_page.click_comment_input()
    homework_page.enter_comment_input("1")
    homework_page.click_send_comment()


    home_page.click_coworking_section()
    time.sleep(2)

    coworking_page = CoworkingPage(driver_firefox)
    coworking_page.click_btn_cw_sign_up()
    time.sleep(2)
    coworking_page.click_chb_filial()
    time.sleep(2)
    coworking_page.click_chb_room()
    time.sleep(2)

    coworking_page.click_btn_select()
    time.sleep(2)

    coworking_page.click_btn_date()
    time.sleep(2)

    coworking_page.click_group_choose()
    time.sleep(2)

    coworking_page.click_chb_select_group()
    time.sleep(2)

    coworking_page.click_btn_select_group()
    time.sleep(2)

    coworking_page.click_time_choose()
    time.sleep(2)

    coworking_page.click_btn_time_choose()
    time.sleep(2)

    coworking_page.click_place_choose()
    time.sleep(2)

    coworking_page.click_chb_place()
    time.sleep(2)

    coworking_page.click_btn_place_choose()
    time.sleep(2)

    coworking_page.click_btn_send()
    time.sleep(2)

    coworking_page.click_btn_cancel()
    time.sleep(2)

    coworking_page.click_btn_confirm_cancel()
    time.sleep(2)


    home_page.click_profile_icon()
    time.sleep(2)
    home_page.click_btn_exit()
    time.sleep(2)
    home_page.click_btn_confirm_exit()

