import time
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By

class FindButtons():
    def __init__(self, driver):
        self.driver = driver

    def __findSchoolBtn(self):
        school_button = self.driver.find_element(by=By.CSS_SELECTOR, value="#rec443991956 > div > div > div > div > div > div.t807__question.js-vote-question > div.t807__answers > div:nth-child(21) > div.t-radio__wrapper > label > div")
        return school_button

    def __findSendingBtn(self):
        send_button = self.driver.find_element(by=By.CSS_SELECTOR, value="#rec443991956 > div > div > div > div > div > div.t807__btn-wrapper > a")
        return send_button
    def pressButtons(self):
        findBtn = FindButtons(self.driver)
        findBtn.__findSchoolBtn().click()
        time.sleep(1)
        findBtn.__findSendingBtn().click()

