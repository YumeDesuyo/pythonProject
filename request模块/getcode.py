# import requests
#
# from selenium import webdriver
# from bs4 import BeautifulSoup
#
# url = 'http://awcoc.com/'
# driver = webdriver.Chrome()
# driver.get(url)
# element = driver.find_element_by_id('verImg')
# element_value = element.text
# driver.quit()
#
# soup = BeautifulSoup(requests.get(url).text, 'html.parser')
# element_value = soup.find('span', {'id': 'verImg'}).text
#
# print(element_value)


import requests
from selenium import webdriver
from bs4 import BeautifulSoup

url = 'http://awcoc.com/'
driver = webdriver.Chrome()
driver.get(url)
element = driver.find_element_by_id('verImg')
element_value = element.text
driver.quit()

soup = BeautifulSoup(requests.get(url).text, 'html.parser')
element_value = soup.find('span', {'id': 'verImg'}).text

print(element_value)
