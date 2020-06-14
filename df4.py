from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

MUS = {
	"Celerio":9217,
	"Celerio X":9217,
	"Swift":18795,
	"Dzire":19073,
	"Ertiga":6352,
	"Vitara Brezza":13172,
	"Ignis":1721,
	"Baleno":16717,
	"Ciaz":2934,
	"S-Cross":2420
}
pop = {}
tot = 0
dem = []
df = pd.read_csv('car_updated.csv')
print("Starting script...")
driver = webdriver.Chrome('D:/Downloads/chromedriver_win32/chromedriver.exe')
driver.maximize_window()
driver.get("https://worldpopulationreview.com/countries/india-population/cities/")
#link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Read Full News")))
#ActionChains(browser).move_to_element(link).perform()
#link.click()
#driver.find_element_by_xpath('.//span[@class="readFull0 hover fullBtn"]').click()
# driver.implicitly_wait(2)
table = driver.find_element_by_xpath('//table[@class="datatableStyles__StyledTable-bwtkle-1 cyosFW table table-striped"]')

for loc in list(set(list(df['location']))):
	if loc == "Gurugram":
		loc = "Gurgaon"
	row = table.find_element_by_xpath("//tr[td='"+loc+"']/td/following-sibling::td[1]")
	x = row.text
	x = x.replace(',','')
	x = int(x)
	if loc=="Gurgaon":
		pop["Gurugram"] = x
	else:
		pop[loc] = x
	tot+=x

for i in range(len(df['car'])):
	dem.append(round(pop[df['location'][i]]*MUS[df['car'][i]]/tot))

df['Monthly Units Sold'] = dem
df.to_csv("delay6.1.csv")