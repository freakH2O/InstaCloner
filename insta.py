import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


u=input('enter your username for instagram')
p=input('enter your instagram password')
usernama=input('enter the username whose posts you want to copy enter in the format without @ and simple name ')
posta=int(input('enter the number of posts the target account has'))


options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument('user-data-dir= selenium')
browser = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')
try:
    browser.get('https://www.instagram.com/accounts/login/?hl=en')
    time.sleep(7)
    us = browser.find_element_by_name('username')
    us.send_keys(u)
    passs = browser.find_element_by_name('password')
    passs.send_keys(p, Keys.ENTER)
except Exception:
    relay=True

browser.get('https://www.instagram.com/'+usernama)

time.sleep(8)
html = browser.find_element_by_tag_name('html')

html.send_keys(Keys.ARROW_DOWN)
time.sleep(0.5)
html.send_keys(Keys.ARROW_DOWN)
time.sleep(0.5)
html.send_keys(Keys.ARROW_DOWN)
time.sleep(0.5)
html.send_keys(Keys.ARROW_DOWN)

#========================================================================================================
try:
    time.sleep(2)
    pyautogui.click(333, 547)  # clciking on first picture

    time.sleep(1)
    pic = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/article/div[1]/div/div[1]/div[2]').screenshot(
        '1.png')
    description = browser.find_element_by_xpath(
        '/html/body/div[2]/div/div[2]/div/article/div[2]/div[1]/ul/li/div/div/div/span').text
    f = open("1.txt", mode='w', encoding='utf-8')
    f.write(description)
    f.close()
    html.send_keys(Keys.ARROW_RIGHT)
    time.sleep(2)
except Exception:
    relay=True
#========================================================================================================


try:
    time.sleep(1)
    pic2 = browser.find_element_by_xpath(
        '/html/body/div[2]/div/div[2]/div/article/div[1]/div/div[1]/div[2]').screenshot('2.png')
    description2 = browser.find_element_by_xpath(
        '/html/body/div[2]/div/div[2]/div/article/div[2]/div[1]/ul/li/div/div/div/span').text
    f = open("2.txt", mode='w', encoding='utf-8')
    f.write(description2)
    f.close()
    html.send_keys(Keys.ARROW_RIGHT)
    time.sleep(3)
except Exception:
    relay=True
#========================================================================================================




try:
    pic3 = browser.find_element_by_xpath(
        '/html/body/div[2]/div/div[2]/div/article/div[1]/div/div[1]/div[2]').screenshot('3.png')
    description3 = browser.find_element_by_xpath(
        '/html/body/div[2]/div/div[2]/div/article/div[2]/div[1]/ul/li/div/div/div/span').text
    f = open("3.txt", mode='w', encoding='utf-8')
    f.write(description3)
    f.close()
    html.send_keys(Keys.ARROW_RIGHT)
except Exception:
    relay=True

#========================================================================================================
relay=True
i=4
while i<=posta:

    time.sleep(2)
   # ========================================================================================================
    try:

      time.sleep(3)
      pic = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/article/div[1]/div/div[1]/div[2]').screenshot(str(i) + '.png')
      description = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/article/div[2]/div[1]/ul/li/div/div/div/span').text
      f = open(str(i) + ".txt", mode='w', encoding='utf-8')
      f.write(description)
      f.close()
      html.send_keys(Keys.ARROW_RIGHT)
      # clicking to close
      i += 1

    except Exception:
      html.send_keys(Keys.ARROW_RIGHT)
      # clicking to close
      relay=True
    # ========================================================================================================

    try:

        time.sleep(3)
        pic2 = browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/article/div[1]/div/div[1]/div[2]').screenshot(str(i) + '.png')
        description2 = browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/article/div[2]/div[1]/ul/li/div/div/div/span').text
        f = open(str(i) + ".txt", mode='w', encoding='utf-8')
        f.write(description2)
        f.close()
        html.send_keys(Keys.ARROW_RIGHT)
        i += 1
    except Exception:
        html.send_keys(Keys.ARROW_RIGHT)
        relay=True
    # ========================================================================================================
    try:

        time.sleep(3)
        pic3 = browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/article/div[1]/div/div[1]/div[2]').screenshot(str(i) + '.png')
        description3 = browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/article/div[2]/div[1]/ul/li/div/div/div/span').text
        f = open(str(i) + ".txt", mode='w', encoding='utf-8')
        f.write(description3)
        f.close()
        html.send_keys(Keys.ARROW_RIGHT)
        i += 1

    except Exception:
        html.send_keys(Keys.ARROW_RIGHT)
        continue
    # ========================================================================================================






























#screen resolution at 1366*768
import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#userno=int(input("enter the number of the user's posts you want to clone from the start "))



try:
    browser.get('https://www.instagram.com/accounts/login/?hl=en')
    time.sleep(5)
    username = browser.find_element_by_name('username')
    username.send_keys(u)
    password = browser.find_element_by_name('password')
    password.send_keys(p, Keys.ENTER)
    time.sleep(5)

except Exception:
    relay=True
relay=True
g=posta
i=1
while i<=posta:
    with open(str(g) + '.txt', 'r',encoding='utf-8') as myfile:
        desc = myfile.read()
        myfile.close()

    browser.get('https://www.instagram.com/'+u)
    time.sleep(15)
    #pyautogui.click(826,226)  # clicking on extension
    extension = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/button')
    extension.click()

    time.sleep(1)

    pyautogui.click(575, 319)  # clicking on add to profile button
    time.sleep(7)
    pyautogui.click(280, 419)  # clicking on windows name selection field
    pyautogui.typewrite(str(g) + '.png')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(5)
    pyautogui.click(818, 426)  # clicking on next image button
    time.sleep(45)
    pyautogui.click(614,468)#clicking caption field
    time.sleep(1)

    pyautogui.typewrite(desc)
    time.sleep(3)
    pyautogui.click(815, 423)  # clicking next button
    time.sleep(10)
    g=g-1
    

