Scrapping the Input Crunchbase URL.

## Installing the requirements.txt 
~~~
 pip install -r requirements.txt
~~~
## Download Chrome Driver depending on your operating system
- <a herf="https://chromedriver.storage.googleapis.com/index.html?path=87.0.4280.88/"> Chrome Driver Download Link </a>
- Set the path of the chrome driver in the script <br> eg. DRIVER_PATH = '.../Documents/Webscrap-crunchbase/crunchbase/chromedriver'


## Input the URL for scrapping in the script
eg : LINK = 'https://www.crunchbase.com/discover/organization.companies/340df1d3bdbb2470c9d204aa71994d5d'

## Running the dashboard on local machine
~~~
 python ful_scrap.py
~~~

## Result:
Downloads the results as a "output.csv".
