from selenium import webdriver
import time

username = '6360031049'
password = 'yokujo07'

url = 'https://www.facebook.com/'

driver = webdriver.Chrome("E:\Python Programs\chromedriver")

driver.get(url)

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)

time.sleep(2)

driver.find_element_by_id('loginbutton').click()

