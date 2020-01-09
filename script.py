import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from bs4 import BeautifulSoup as b
import constant
import pages

driver = 0
search_name = 'auctux' #your search on goolgle here

def main():

	global driver

	for x in range(0, 2000):
		try:
			driver = webdriver.Chrome('D:/chromedriver.exe')
			time.sleep(2)
			runner = pages.Pages(driver, search_name)
			runner.route()
			time.sleep(2)
			print('looking for ', search_name)
			runner.goto()
			time.sleep(2)
			print(x, 'window')
			driver.close()
			time.sleep(1)
		except:
			print("something went wrong !ERROR!")

	time.sleep(60)
	print('you made it ! Congrat')
	

if __name__=='__main__':
	main()