import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument('user-data-dir= selenium')
browser = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')
browser.get('https://chrome.google.com/webstore/detail/upload-photo-to-instagram/oknpgmaeedlbdichgaghebhiknmghffa?hl=en')
time.sleep(10)
add=browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[2]/div/div/div/div')
add.click()

time.sleep(5)
pyautogui.click(662,277)#Add Extension
