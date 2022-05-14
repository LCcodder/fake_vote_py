
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from buttons import FindButtons
import time
from browsermobproxy import Server
import urlparse

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")


options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url = "http://kino.mosmetod.ru/golosovanie_trailer"


driver.get(url)
time.sleep(2)

findbtns = FindButtons(driver)
findbtns.pressButtons()

time.sleep(1)
driver.quit()


