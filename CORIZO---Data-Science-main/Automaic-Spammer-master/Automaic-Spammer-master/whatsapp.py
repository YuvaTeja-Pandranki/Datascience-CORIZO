from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome('C:/Users/HCL/Downloads/chromedriver') 
driver.get("https://web.whatsapp.com/") 

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
#//*[@id="pane-side"]/div[1]/div/div/div[15]/div/div/div[2]/div[1]/div[1]/div/span
#
user.click()

msg_box = driver.find_element_by_class_name('_2S1VP copyable-text selectable-text')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()

# earlier iteration of my code
'''
name = "tuptup" # enter the name of contact as saved in your device
msg = "ok" # enter the message that you want to send
count = 10000 # enter the count of times you want to spam with

input("Enter any key after the scanning is done")

user = driver.find_element_by_xpath("_3H4MS")
user.click()

msg_box = driver.find_element_by_class_name("_3u328")

for i in range(count):
	msg_box.send_keys(msg)
	button = driver.find_element_by_class_name("hjJpn")
	button.click()

'''
