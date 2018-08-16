# Crawler to get meteorological data from INMET (Instituto Nacional de Meteorologia), Brazil.
It's simple crawler to get the data, save on sqlite lite, and can be export to csv.

1. How do I get set up? Set up Install python 3.x and Create a virtualenv:
[See here how to](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/)

2. Install all requeriments to use:
	```
	user@server:~$ pip install -r requirements
	```
3.  Create tables and import base data:
    ```
	user@server:~$ python create_tables.py && python import_weather_stations.py && python import_wind_directions.py
	```
4. Change the config before crawling:
	Step 1: Create a login on INMET ( you will need an account ): [See here how to](http://www.inmet.gov.br/projetos/rede/pesquisa/cad_senha.php)

	Step 2: Set user/pass (config.py)
    ```
    USER = 'email@xpto.com'
    PASS = '123456'
    ```

5. Change the string DATABASE_URI on config.py editing for DATABASE_URI = 'sqlite:////tmp/climate.db'
  
6. Crawling!! (Follow progress in crawler.log)
    ```
	user@server:~$ python crawler_data.py
	```
	
7. Change the query in export_data.py as you need to export to csv and run:
    ```
	user@server:~$ python export_data.py
	```


## WebDrive

This project is based in PhantomJS to do the crawler. If do you want change for another webdriver this is a list of suported drives below and line for change is 20 from crawler_data.py .

* webdriver.Firefox
* webdriver.FirefoxProfile
* webdriver.Chrome
* webdriver.ChromeOptions
* webdriver.Ie
* webdriver.Opera
* webdriver.PhantomJS
* webdriver.Remote
* webdriver.DesiredCapabilities
* webdriver.ActionChains
* webdriver.TouchActions
* webdriver.Proxy


Install PhantomJS

Tutorial how install PhantomJS [gist - Tutorial](https://gist.github.com/julionc/7476620)

