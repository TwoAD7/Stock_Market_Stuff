from selenium import webdriver 
from time import sleep
#import urllib2
#from bs4 import BeautifulSoup #used to pull dat
import pandas as pd




"""
Roy Salinas
Updated 08/30/2020
Webdriver version (Microsoft Edge): Version 84.0.522.63 (Official build) (64-bit)

Purpose: To read in Russell 2000 company data with some fundamental values

Helpful links:

https://stackoverflow.com/questions/37090653/iterating-through-table-rows-in-selenium-python
https://selenium-python.readthedocs.io/locating-elements.html
https://money.cnn.com/data/markets/russell/?page=1

"""
#Function to read in data 

names =[]
price = []
pe_rat = [] 
def get_row_data(table):
	temp = []
  	for row in table.find_elements_by_xpath(".//tr"):
   		#yield [td.text for td in row.find_elements_by_xpath(".//td")] #yield is used to return a sequence of things 
   	 	temp.append([td.text for td in row.find_elements_by_xpath(".//td")])
 	temp.pop(0) #get rid of empty array 
	return temp 

def grab_comp_info():
	for i in range(1,79):
		url = "https://money.cnn.com/data/markets/russell/?page=%d" % i
		driver = webdriver.Edge(executable_path="/mnt/c/Users/Owner/Desktop/Folders/python/msedgedriver.exe") #the driver that is being used to launch google chrome, depends on the search engine you're using. 
		driver.get(url)	#driver now holds the html webdriver of CNN Business 
		#driver.close()
		driver.minimize_window()
		print("Opened CNN Business Russell 2000 for page %d" % i)
		sleep(6)

		tables = driver.find_elements_by_xpath("//table[@class='wsod_dataTable wsod_dataTableBig']") #table containing data 
		"""
		'tables' has three instances, in this case. There are three tags with the "table" tag with the same class attribute. The third one (2) 
		is the one we want
		"""
		for i in get_row_data(tables[2]):
			#print(i)
			names.append(str(i[0]))
			price.append(str(i[1]))
			pe_rat.append(str(i[4]))
		driver.close()

if __name__ == "__main__": #if its run as a script by itself in shell (python Russell_2000_CSV.py)
	grab_comp_info()
	df = pd.DataFrame({"Name":names,"Price":price,"P/E": pe_rat})
	print(df)
	df.to_csv("Russell_2000.csv",sep=',',index=False)

def R2000_data(): #run while not being main in other scripts. Being called in other function
	print("Grabbing data...\n")
	grab_comp_info()
	df = pd.DataFrame({"Name":names,"Price":price,"P/E": pe_rat})
	df.to_csv("Russell_2000.csv",sep=',',index=False)


