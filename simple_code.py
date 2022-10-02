import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
print('opening a page in chrome browser')
time.sleep(5)
url = 'https://the-internet.herokuapp.com/login'
print('getting website')
time.sleep(5)
driver.get(url)

'''
Lets find Xpath on 'Inspect'
login - //*[@id="username"]
password - //*[@id="password"]
button - //*[@id="login"]/button
'''

driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('tomsmith')
time.sleep(5)
print('sending username')
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('SuperSecretPassword!')
print('sending password')
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="login"]/button').click()
print('Mission is complete')
time.sleep(5)
driver.quit()
