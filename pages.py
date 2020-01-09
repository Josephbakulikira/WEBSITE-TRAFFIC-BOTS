import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from bs4 import BeautifulSoup as b

class Pages:
	def __init__(self, driver, search_name):
		self.driver = driver
		self.search_name = search_name

	def route(self):
		
		self.driver.get('https://www.google.com/')
		time.sleep(3)

		searcher = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')))
		searcher.click()
		searcher.send_keys(self.search_name)

		self.driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input").send_keys(Keys.ENTER)
		time.sleep(2)

	def goto(self):
		searcher = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="rso"]/div[1]/div/div[1]/div/div/div[1]/a/h3')))
		searcher.click()
		time.sleep(3)
		print('welcome to AUCTUX WEBSITE')
		time.sleep(1)





		
