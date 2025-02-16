from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get("https://inventwithpython.com")

try:
    # Явное ожидание, пока все элементы с классом 'row' не станут доступными
    elements = WebDriverWait(browser, 10).until(
       EC.presence_of_all_elements_located((By.CLASS_NAME, 'row'))
    )
    found_elements = [elem.text for elem in elements]
    for elem in elements:
        print('Find Element <%s> succeeded!' % (elem.location))
except Exception as e:
    print('Find Element failed!', e)
print('Found elements:', found_elements, 'Privet')