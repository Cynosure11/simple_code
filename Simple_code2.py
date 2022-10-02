import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
print('opening a page in chrome browser')
time.sleep(5)

'''
Another simple example how selenium works 
'''

print('Another exercise...')
time.sleep(2)
url_2 = 'https://the-internet.herokuapp.com/dynamic_loading/2'
driver.get(url_2)
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="start"]/button').click()
driver.implicitly_wait(10)

finish_text = driver.find_element(By.XPATH, '//*[@id="finish"]').text
print(finish_text)
time.sleep(5)


driver.quit()

