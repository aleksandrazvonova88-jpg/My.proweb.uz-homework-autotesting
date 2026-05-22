from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class CoworkingPage:
    def __init__(self, driver):
        self.driver = driver
        self.btn_cw_sign_up = (By.CSS_SELECTOR, '#app > div > div.coworking > div > button')
        self.chb_filial = (By.CSS_SELECTOR, '#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div.container.coworking__page-dialog-follow-container > div.coworking__page-dialog-follow-branch > div:nth-child(2) > div.list-tile.coworking__page-dialog-follow-branch-item-list > div.list-tile__trailing')
        self.chb_room = (By.CSS_SELECTOR, '#dialog > div.material-dialog.coworking__branch-dialog > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div > div:nth-child(1) > div.list-tile__trailing > button')
        self.btn_select = (By.CSS_SELECTOR, '#dialog > div.material-dialog.coworking__branch-dialog > div > div.material-dialog__window-actions > button:nth-child(2)')
        self.btn_date = (By.CSS_SELECTOR, '#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div.container.coworking__page-dialog-follow-container > div.coworking__page-dialog-follow-date > div > div:nth-child(4) > button')
        self.group_choose = (By.CSS_SELECTOR, '#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div.container.coworking__page-dialog-follow-container > div.list-tile.coworking__page-dialog-follow-list')
        self.chb_select_group = (By.CSS_SELECTOR, '#dialog > div:nth-child(2) > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div > div > div.list-tile__trailing > button')
        self.btn_select_group = (By.CSS_SELECTOR, '#dialog > div:nth-child(2) > div > div.material-dialog__window-actions > button:nth-child(2)')
        self.time_choose = (By.CSS_SELECTOR, '#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div.container.coworking__page-dialog-follow-container > div.coworking__page-dialog-follow-timeseat > div:nth-child(1) > label > input')
        self.btn_time_choose = (By.CSS_SELECTOR, '#dialog > div.material-dialog.timepicker > div > div.material-dialog__window-actions > button:nth-child(2)')
        self.place_choose = (By.CSS_SELECTOR, '#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div.container.coworking__page-dialog-follow-container > div.coworking__page-dialog-follow-timeseat > div:nth-child(2) > div')
        self.chb_place = (By.CSS_SELECTOR, '#dialog > div:nth-child(2) > div > div.material-dialog__window-container > div.material-dialog__window-body > div.coworking__page-dialog-time-seats > div:nth-child(1) > div.list-tile__trailing > button')
        self.btn_place_choose = (By.CSS_SELECTOR, '#dialog > div:nth-child(2) > div > div.material-dialog__window-actions > button:nth-child(2)')
        self.btn_send = (By.CSS_SELECTOR, '#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)')
        self.btn_cancel = (By.CSS_SELECTOR, '#app > div > div.coworking > div > div.lazyscroll > div > div > div:nth-child(9) > div > div.flex.aic.jcsb.width100.gap5 > button')
        self.btn_confirm_cancel = (By.CSS_SELECTOR, '#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)')

    def click_btn_cw_sign_up(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_cw_sign_up)).click()

    def click_chb_filial(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.chb_filial)).click()

    def click_chb_room(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.chb_room)).click()
    def click_btn_select(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_select)).click()
    def click_btn_date(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_date)).click()
    def click_group_choose(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.group_choose)).click()
    def click_chb_select_group(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.chb_select_group)).click()
    def click_btn_select_group(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_select_group)).click()
    def click_time_choose(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.time_choose )).click()
    def click_btn_time_choose(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_time_choose)).click()
    def click_place_choose(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.place_choose)).click()
    def click_chb_place(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.chb_place)).click()
    def click_btn_place_choose(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_place_choose)).click()
    def click_btn_send(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_send)).click()
    def click_btn_cancel(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_cancel)).click()
    def click_btn_confirm_cancel(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_confirm_cancel)).click()



