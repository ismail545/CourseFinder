# Pip install Selenium, and install chromedriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

browser = webdriver.Chrome('chromedriver.exe')

if sys.argv[1] == "emb":
    browser.get('https://huddersfield.brightspace.com/d2l/le/content/66899/Home')
if sys.argv[1] == "apd":
    browser.get('https://huddersfield.brightspace.com/d2l/le/content/66091/Home')
if sys.argv[1] == "maths":
    browser.get('https://huddersfield.brightspace.com/d2l/le/content/66050/Home')
if sys.argv[1] == "ops":
    browser.get('https://huddersfield.brightspace.com/d2l/le/content/66113/Home')
if sys.argv[1] == "oos":
    browser.get('https://huddersfield.brightspace.com/d2l/le/content/66085/Home')
if sys.argv[1] == "database":
    browser.get('https://huddersfield.brightspace.com/d2l/le/content/66102/Home')
if sys.argv[1] == "proj":
    browser.get('https://huddersfield.brightspace.com/d2l/le/content/65998/Home')

login_name = browser.find_element_by_id("userName")
Username = 'Username'
# The user would enter his username and password into the code
Password = 'password'
login_name.send_keys(Username)

login_password = browser.find_element_by_id(Password)

login_password.send_keys("Amazing123")

login_button = browser.find_element_by_class_name("d2l-button")
login_button.click()


