from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get('http://login.metafilter.com')


try:
    # Явное ожидание, пока элемент с текстом ссылки 'Read It Online' не станет доступным
    linkElem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Read Online for Free'))
    )
    print('Find Element succeeded!')
    linkElem.click()
except Exception as e:
    print('Find Element failed!', e)