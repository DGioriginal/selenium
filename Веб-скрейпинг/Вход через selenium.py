from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get('https://login.metafilter.com/logging-in.mefi')

try:
    # Явное ожидание, пока элемент с ID 'user_name' не станет доступным
    userElem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'user_name'))
    )
    print('Find Element succeeded!')
    userElem.send_keys('username')

    # Явное ожидание, пока элемент с ID 'user_pass' не станет доступным
    passwordElem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'user_pass'))
    )
    passwordElem.send_keys('password')
    passwordElem.submit()
except Exception as e:
    print('Find Element failed!', e)

# Добавить паузу, чтобы браузер оставался открытым
import time
time.sleep(10)  # Ожидание 10 секунд

# Закрыть браузер после паузы
browser.quit()