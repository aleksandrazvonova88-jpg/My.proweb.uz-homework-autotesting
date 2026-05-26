from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class LessonsPage:
    def __init__(self, driver):
        self.driver = driver
        self.btn_lessons = (By.CSS_SELECTOR, '#tabbar > div > div.tab-header > div.tab-header__wrapper > div:nth-child(2)')
        self.lesson_card = (By.CSS_SELECTOR, '#app > div > div.container.container_mobile > div > div > div.new-lessons_content > div > div:nth-child(5) > div.flex.gap20 > div:nth-child(3) > div.lesson-card')
        self.btn_play_video = (By.CSS_SELECTOR, '#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button')
        # self.btn_fullscreen = (By.CSS_SELECTOR, '#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls.video-player-proweb__controlls-hidden > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button:nth-child(3)')
        self.btn_fullscreen = (By.CSS_SELECTOR, 'div.video-player-proweb__controllers-right > button:nth-child(3)')
        self.btn_fullscreen_ff = (By.CSS_SELECTOR, 'button.video-player-proweb__controllers-container:nth-child(2)')
        self.press_video = (By.CSS_SELECTOR, '#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__actinview')
        # self.btn_pause = (By.CSS_SELECTOR, '#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls.video-player-proweb__controlls-hidden > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button')
        self.btn_pause = (
            By.CSS_SELECTOR,
            'button.video-player-proweb__controllers-play'
        )
        # self.fullscreen_exit = (By.CSS_SELECTOR, '#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls.video-player-proweb__controlls-hidden > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button:nth-child(3) > span')
        self.fullscreen_exit = (By.CSS_SELECTOR, 'div.video-player-proweb__controllers-right > button:nth-child(3)')
        self.fullscreen_exit_ff = (By.CSS_SELECTOR, 'button.video-player-proweb__controllers-container:nth-child(2)')
        self.rating = (By.CSS_SELECTOR, '#app > div > div.videolesson > div > div:nth-child(2) > div > div.videolesson__general-footer-rating.mb10 > div > div > div > span:nth-child(5)')
        self.send_rating = (By.CSS_SELECTOR, '#dialog > div > div > div > div > div > button')
        self.btn_back = (By.CSS_SELECTOR, '#app > div > div.videolesson > div > div:nth-child(2) > div > div.back-to-less.back-to-less-lesson')

    def show_controls(self):
        video = self.driver.find_element(*self.press_video)

        ActionChains(self.driver).move_to_element(video).perform()

    def click_btn_lessons(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_lessons)).click()
    def click_lesson_card(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.lesson_card)).click()
    def click_btn_play_video(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_play_video)).click()
    # def click_btn_fullscreen(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.element_to_be_clickable(self.btn_fullscreen)).click()
    def click_btn_fullscreen(self):
        self.show_controls()

        wait = WebDriverWait(self.driver, 10)

        fullscreen_btn = wait.until(
            EC.element_to_be_clickable(self.btn_fullscreen)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            fullscreen_btn
        )

    def click_btn_fullscreen_ff(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_fullscreen_ff)).click()

    def click_press_video(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.press_video)).click()
    # def click_btn_pause(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.element_to_be_clickable(self.btn_pause)).click()

    def click_btn_pause(self):
        self.show_controls()

        time.sleep(1)

        pause_btn = self.driver.find_element(*self.btn_pause)

        self.driver.execute_script(
            "arguments[0].click();",
            pause_btn
        )
    # def click_fullscreen_exit(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.element_to_be_clickable(self.fullscreen_exit)).click()
    # def click_fullscreen_exit(self):
    #     self.show_controls()
    #
    #     wait = WebDriverWait(self.driver, 10)
    #
    #     exit_btn = wait.until(
    #         EC.element_to_be_clickable(self.fullscreen_exit)
    #     )
    #
    #     self.driver.execute_script(
    #         "arguments[0].click();",
    #         exit_btn
    #     )
    # def click_fullscreen_exit(self):
    #     self.driver.find_element("tag name", "body").send_keys(Keys.ESCAPE)
    # def click_fullscreen_exit(self):
    #     video = self.driver.find_element(*self.press_video)

    # def click_fullscreen_exit(self):
    #     video = self.driver.find_element(*self.press_video)
    #
    #     video.click()
    #
    #     video.send_keys(Keys.ESCAPE)
    #
    #     video.send_keys(Keys.ESCAPE)

    def click_fullscreen_exit(self):
        self.driver.execute_script("""
            if (document.fullscreenElement) {
                document.exitFullscreen();
            }
        """)

    def click_fullscreen_exit_ff(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.fullscreen_exit_ff)).click()

    def click_rating(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.rating)).click()
    def click_send_rating(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.send_rating)).click()

    def click_btn_back(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_back)).click()