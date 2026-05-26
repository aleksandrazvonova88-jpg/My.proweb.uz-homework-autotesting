from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.login=(By.CSS_SELECTOR, '#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-center > div > label > input')
        self.btn_uz = (By.CSS_SELECTOR, '#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-bot-langs > div:nth-child(2)')

        self.btn_login=(By.CSS_SELECTOR, '#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-bot > button')
        self.password=(By.CSS_SELECTOR, '#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-center.log-in__newContent-right-block-center-checkpass > div.log-in__newContent-right-block-center-inp > label')
        self.password_ff = (By.CSS_SELECTOR, '.material-input__input')
        self.btn_submit=(By.CSS_SELECTOR, '#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-bot > button')
        self.btn_session=(By.CSS_SELECTOR, '#dialog > div > div > div > div.material-dialog__window-body.material-dialog__window-body_modify > div > div:nth-child(2) > div > div > div.list-tile__trailing > button')
        self.btn_session_edge = (By.CSS_SELECTOR, '#dialog > div > div > div > div.material-dialog__window-body.material-dialog__window-body_modify > div > div:nth-child(2) > div > div > div.list-tile__trailing > button')
        self.btn_session_ff = (By.CSS_SELECTOR, 'div.drop-down-component:nth-child(2) > div:nth-child(1) > div:nth-child(1)')
        self.btn_finish=(By.CSS_SELECTOR, '#dialog > div > div > div > div.material-dialog__window-body.material-dialog__window-body_modify > div > div:nth-child(2) > div.drop-down-component__content > div.sessions__item-content > button')
        self.btn_finish_edge = (By.CSS_SELECTOR, '#dialog > div > div > div > div.material-dialog__window-body.material-dialog__window-body_modify > div > div:nth-child(2) > div.drop-down-component__content > div.sessions__item-content > button')
        self.btn_finish_ff = (By.CSS_SELECTOR, '.material-filled-button')
    def enter_login(self, login):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.login)).send_keys(login)

    def click_btn_uz(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.element_to_be_clickable(self.btn_uz)).click()
    def click_btn_login(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_login)).click()
    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.password)).send_keys(password)
    def enter_password_ff(self, password):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.password_ff)).send_keys(password)
    def click_btn_submit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_submit)).click()
    def click_btn_session(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_session)).click()
    def click_btn_session_edge(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_session_edge)).click()
    # def click_btn_session_ff(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.element_to_be_clickable(self.btn_session_ff)).click()

    # def click_btn_session_ff(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     button = wait.until(EC.element_to_be_clickable(self.btn_session_ff))
    #
    #     self.driver.execute_script(
    #         "arguments[0].click();",
    #         button
    #     )

    def click_btn_session_ff(self):
        wait = WebDriverWait(self.driver, 15)
        button = wait.until(EC.visibility_of_element_located(self.btn_session_ff))
        actions = ActionChains(self.driver)
        actions.move_to_element(button).pause(1).click().perform()
    def click_btn_finish_edge(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_finish_edge)).click()
    def click_btn_finish_ff(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_finish_ff)).click()

    def click_btn_finish(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_finish)).click()

