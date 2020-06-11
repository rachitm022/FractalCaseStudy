from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

print("Starting script...")
driver = webdriver.Chrome('D:/Downloads/chromedriver_win32/chromedriver.exe')
driver.maximize_window()
df = pd.read_csv("delay2.csv")
prices = []
cities = list(set(list(df["location"])))
car = list(set(list(df["car"])))
#dict = {}
for i in range(len(df['car'])):
	#dict[city] = {}
	link  = "https://www.cardekho.com/maruti-"
	link += (str(df['car'][i]).strip().lower())
	link += "/car-price-in-"
	link += ((str(df['location'][i]).strip().lower())+".htm")
	print(link)
	driver.get(link)
	#link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Read Full News")))
	#ActionChains(browser).move_to_element(link).perform()
	#link.click()
	try:
		x = driver.find_element_by_xpath(".//td[contains(@class, 'gsc_col-xs-4 gsc_col-md-')]").text
		x = x.split('*')[0]
		x = x.split('.')[1]
		print(x)
		prices.append(x)
		# driver.implicitly_wait(2)
	except:
		print('Exception occured')
		prices.append('nan')
	
df['price'] = prices
df.to_csv("delay3.csv")