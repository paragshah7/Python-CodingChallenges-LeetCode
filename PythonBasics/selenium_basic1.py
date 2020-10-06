# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# browser = webdriver.Chrome('/Users/paragshah/Downloads/chromedriver')

browser = webdriver.Firefox()
browser.maximize_window()

browser.get('https://www.seleniumhq.org/')
pageTitle = browser.title
assert 'Selenium' in pageTitle, 'Title mismatch'

elem = browser.find_element_by_link_text('Download')
print(elem.get_attribute('href'))
elem.click()

searchBar = browser.find_element_by_id('q')
searchBar.send_keys('geckodriver')
searchBar.send_keys(Keys.ENTER)

WebDriverWait(browser, 5).until(EC.alert_is_present())
alertPop = browser.switch_to.alert
time.sleep(3)
alertPop.accept()
time.sleep(5)

browser.quit()
