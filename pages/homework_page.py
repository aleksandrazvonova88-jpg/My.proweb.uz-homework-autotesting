from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class HomeworkPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.homeworks = (By.CSS_SELECTOR, '#tabbar > div > div > div.tab-header__wrapper > div:nth-child(4)')
        self.homework_dd = (By.CSS_SELECTOR, '#app > div > div.container.container_mobile > div > div > div.tab-content.group-homeworks-tab-content > div > div > div > div:nth-child(3) > div.work-dropdown.homework-card_drop.grow > div')
        self.go_to_homework = (By.CSS_SELECTOR, '#app > div > div.container.container_mobile > div > div > div.tab-content.group-homeworks-tab-content > div > div > div > div:nth-child(3) > div.work-dropdown.homework-card_drop.grow.homework-card_drop-active > div.work-dropdown-content > div > button')
        self.comment_input = (By.CSS_SELECTOR, '#app > div > div.container.homework-page-container > div > div > div > div.solved-homework__materials > div.message-input.relative.solved-homework-input > div > div > label > textarea')
        self.send_comment = (By.CSS_SELECTOR, '#app > div > div.container.homework-page-container > div > div > div > div.solved-homework__materials > div.message-input.relative.solved-homework-input > button')

    def click_homeworks(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.homeworks)).click()

    def click_homework_dd(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.homework_dd)).click()

    def click_go_to_homework(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.go_to_homework)).click()

    def click_comment_input(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.comment_input)).click()

    def enter_comment_input(self, comment):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.comment_input)).send_keys(comment)

    def click_send_comment(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.send_comment)).click()