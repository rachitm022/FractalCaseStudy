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
driver.get("https://www.cardekho.com/india-car-news/january-2019-waiting-period-on-maruti-cars-when-can-you-get-delivery-of-new-ertiga-swift-dzire-vitara-brezza-baleno-23018.htm")
#link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Read Full News")))
#ActionChains(browser).move_to_element(link).perform()
#link.click()
driver.find_element_by_xpath('.//span[@class="readFull0 hover fullBtn"]').click()
tables = driver.find_elements_by_class_name("table-responsive")
df = pd.DataFrame(columns=['car','location','delay'])
for table in tables:
	rows = table.find_elements(By.TAG_NAME, "tr") 
	cars = []
	loc = ""
	delay = ""
	for i,row in enumerate(rows):
		if i > 0:
		    cols = row.find_elements(By.TAG_NAME, "td") 
		    for j,col in enumerate(cols):
		    	if i==1 and j>0:
		    		cars.append(col.text)
		    		continue
		    	
		    	if i>1 and j==0:
		    		loc = col.text
		    	
		    	if i>1 and j>0:
		    		delay = col.text
		    		df = df.append({'car':cars[j-1],'location':loc,'delay':delay},ignore_index=True)
		    	
		    	print(col.text)

df.to_csv("delay2.csv")