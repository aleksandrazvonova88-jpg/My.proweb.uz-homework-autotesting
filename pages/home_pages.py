from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class HomePages:
    def __init__(self, driver):
        self.driver = driver
        self.video_instruction=(By.CSS_SELECTOR, '#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-page > div > div.home-card.pointer')
        self.btn_fullscreen=(By.CSS_SELECTOR, '#app > div > div.home-instruction > div > div.home-instruction__content-main > div > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button:nth-child(5)')
        self.btn_fullscreen_ff = (By.CSS_SELECTOR, 'button.video-player-proweb__controllers-container:nth-child(4)')
        self.press_video=(By.CSS_SELECTOR, '#app > div > div.home-instruction > div > div.home-instruction__content-main > div > div > div.video-player-proweb__actinview')
        self.btn_pause = (
            By.CSS_SELECTOR,
            'button.video-player-proweb__controllers-play'
        )
        # self.btn_pause=(By.CSS_SELECTOR, '#app > div > div.home-instruction > div > div.home-instruction__content-main > div > div > div.video-player-proweb__controlls.video-player-proweb__controlls-hidden > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button.video-player-proweb__controllers-play')
##app > div > div.home-instruction > div > div.home-instruction__content-main > div > div > div.video-player-proweb__controlls.video-player-proweb__controlls-hidden > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button.video-player-proweb__controllers-play
        self.fullscreen_exit=(By.CSS_SELECTOR, '#app > div > div.home-instruction > div > div.home-instruction__content-main > div > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button:nth-child(5)')
        ##app > div > div.home-instruction > div > div.home-instruction__content-main > div > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button:nth-child(5)
        self.fullscreen_exit_ff = (By.CSS_SELECTOR, 'button.video-player-proweb__controllers-container:nth-child(4)')
        self.logo=(By.CSS_SELECTOR, '#app > div > div.header > nav > div.header__logo > div > a > h2')
        self.group_card=(By.CSS_SELECTOR, '#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-page > div > div:nth-child(2)')
        self.coworking_section = (By.CSS_SELECTOR, '#app > div > div.layout > div > div.material-dialog__window > div > ul > li:nth-child(3)')
        self.profile_icon=(By.CSS_SELECTOR, '#app > div > div.header > div > div.header__avatar > div')
        self.btn_exit=(By.CSS_SELECTOR, '#app > div > div.inforation > div > div > div:nth-child(4) > div')
        self.btn_confirm_exit=(By.CSS_SELECTOR, '#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)')


    def click_video_instruction(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.video_instruction)).click()

    def click_btn_fullscreen(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_fullscreen)).click()

    def click_btn_fullscreen_ff(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_fullscreen_ff)).click()

    def click_press_video(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.press_video)).click()

    def click_btn_pause(self):
        video = self.driver.find_element(*self.press_video)

        ActionChains(self.driver).move_to_element(video).perform()

        wait = WebDriverWait(self.driver, 10)

        pause_btn = wait.until(
            EC.element_to_be_clickable(self.btn_pause)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            pause_btn
        )

    def click_fullscreen_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.fullscreen_exit)).click()

    def click_fullscreen_exit_ff(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.fullscreen_exit_ff)).click()

    def click_logo(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.logo)).click()

    def click_group_card(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.group_card)).click()

    def click_coworking_section(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.coworking_section)).click()

    def click_profile_icon(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.profile_icon)).click()

    def click_btn_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_exit)).click()

    def click_btn_confirm_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_confirm_exit)).click()




