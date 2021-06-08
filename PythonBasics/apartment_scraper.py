
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pywhatkit
import pyautogui as pg

driver = webdriver.Chrome('/Users/paragshah/PythonCoding/PythonPractice/PythonBasics/chromedriver')
driver.maximize_window()


driver.get('https://www.irvinecompanyapartments.com/content/icac/ica/home/'
            'special-offers/san-jose.html#community=RiverView')
# time.sleep(3)
pageTitle = driver.title
print('Title -', pageTitle)
assert 'San Jose' in pageTitle, 'Title mismatch'

wait = WebDriverWait(driver, 10)
description = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//body[1]/div[1]/main[1]/div[1]/div[2]/div[3]/div[1]/div[1]/p[1]"))).text
print('Description - ', description)

driver.close()
driver.quit()

# WhatsApp Code
if 'April' in description:
    print('** Offer in April **')
    pywhatkit.sendwhatmsg('+14087148625', 'Current Riverview offer still for April', 17, 11)
elif 'May' in description:
    print('** Offer in May **')
    pywhatkit.sendwhatmsg('+14087148625', 'New Riverview offer for May!', 17, 11)