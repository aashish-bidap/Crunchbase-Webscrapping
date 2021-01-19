from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

DRIVER_PATH = '/Documents/Webscrap-crunchbase/crunchbase/chromedriver'
#PATH = '/Documents/Webscrap-crunchbase/crunchbase/html_source.html'
LINK = 'https://www.crunchbase.com/discover/organization.companies/340df1d3bdbb2470c9d204aa71994d5d'

def scrapper(link):
	
	options = Options()
	options.headless = False
	options.add_argument("--window-size=1920,1200")
	driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
	driver.get(link)

	parsed_html = BeautifulSoup(driver.page_source,"html.parser")
	grid_rows = parsed_html.find_all('grid-row')

	rows = []

	for i in grid_rows:

		row_values={}
		grid_cell1 = i.findAll("grid-cell", {"class": "sticky-column-2 column-id-identifier ng-star-inserted"})
		
		#id and name
		for each_element1 in grid_cell1:
			if each_element1.findAll("div", {"class": "flex-none cb-text-color-medium cb-margin-medium-left ng-star-inserted"}):
				my_id = each_element1.findAll("div", {"class": "flex-none cb-text-color-medium cb-margin-medium-left ng-star-inserted"})
				my_name = each_element1.findAll("a")
				id_ = my_id[0].text
				name = my_name[0].text
				
		#category
		grid_cell2 = i.findAll("grid-cell", {"class": "column-id-categories ng-star-inserted"})
		for each_element2 in grid_cell2:
			if each_element2.findAll("a"):
				categories = each_element2.findAll("a")
				category_list=[]
				for cat in categories:
					category = cat.text
					category_list.append(category)

		#location
		grid_cell3 = i.findAll("grid-cell", {"class": "column-id-location_identifiers ng-star-inserted"})
		for each_element3 in grid_cell3:
			locations = each_element3.findAll("a")
			for place in locations:
				location = place.text

		#short description
		grid_cell4 = i.findAll("grid-cell", {"class": "column-id-short_description ng-star-inserted"})
		for each_element4 in grid_cell4:
			desc = each_element4.findAll("span",{"class": "component--field-formatter field-type-text_long ng-star-inserted"})
			for each_desc in desc:
				description = each_desc.text

		#rank
		grid_cell5 = i.findAll("grid-cell", {"class":"column-id-rank_org_company ng-star-inserted"})
		for each_element5 in grid_cell5:
			rank = each_element5.findAll("a")
			for each_rank in rank:
				rank = each_rank.text

		row_values['Id'] = id_
		row_values['Name'] = name
		row_values['Industry'] = category_list
		row_values['Location'] = location
		row_values['Description'] = description
		row_values['Rank'] = rank

		rows.append(row_values)
		
	return rows

if __name__ == "__main__": 
	val = scrapper(LINK)
	df = pd.DataFrame(val)
	df.to_csv("output.csv")
