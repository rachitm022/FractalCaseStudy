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
df = pd.read_csv("delay3.csv")
car = list(set(list(df["car"])))
t = {}
name = ""
df["ARAI Mileage"] = ['nan' for i in range(len(df['car']))]
df["Engine Displacement (cc)"] = ['nan' for i in range(len(df['car']))]
df["Max Torque (nm@rpm)"] = ['nan' for i in range(len(df['car']))]
df["Seating Capacity"] = ['nan' for i in range(len(df['car']))]
df["Boot Space (Litres)"] = ['nan' for i in range(len(df['car']))]
df["Body Type"] = ['nan' for i in range(len(df['car']))]
df["Fuel Type"] = ['nan' for i in range(len(df['car']))]
df["Max Power (bhp@rpm)"] = ['nan' for i in range(len(df['car']))]
df["TransmissionType"] = ['nan' for i in range(len(df['car']))]
df["Fuel Tank Capacity"] = ['nan' for i in range(len(df['car']))]
df["Service Cost (Avg. of 5 years)"] = ['nan' for i in range(len(df['car']))]
tmp = [df['car'][i] for i in range(len(df['car']))]
tmp = list(set(tmp))
for i in range(len(tmp)):
	t[str(tmp[i])] = {}
	link  = "https://www.cardekho.com/maruti/maruti-"
	link += (str(tmp[i]).strip().lower())
	link += "-specifications.htm"
	print(link)
	driver.get(link)
	try:
		table = driver.find_element_by_class_name("keyfeature")
		rows = table.find_elements(By.TAG_NAME, "tr") 
		for row in rows:
			cols = row.find_elements(By.TAG_NAME, "td") 
			for j,col in enumerate(cols):
				if j==0:
					name = col.text
				else:
					t[str(tmp[i])][name] = col.text
	except:
		print('Exception occured')
		for x in t[str(tmp[i])].keys():
			t[str(tmp[i])][x] = 'nan'

for i in range(len(df['car'])):
	for spec,val in t[str(df['car'][i])].items():
		df.loc[i,spec] = val

df.to_csv('delay5.csv')