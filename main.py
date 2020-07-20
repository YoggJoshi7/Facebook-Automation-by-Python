from selenium import webdriver
import time

username = 'your username'
password = 'your password'

url = 'https://www.facebook.com/'

driver = webdriver.Chrome("paste the loaction of your chromedriver")

driver.get(url)

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)

time.sleep(2)

driver.find_element_by_id('loginbutton').click()
