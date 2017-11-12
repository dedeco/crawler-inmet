
import time
import sys
import logging

from datetime import datetime, timedelta

from selenium import webdriver
from bs4 import BeautifulSoup

from config import USER, PASS, LOGIN_URL

from database import Base, engine, session
from database import Weather_station, Measurements_daily, Wind_direction

from utils import datestring_to_date


def login():
	browser = webdriver.PhantomJS()
	browser.get(LOGIN_URL)
	emailElement = browser.find_element_by_name("mCod")
	emailElement.send_keys(USER)
	#time.sleep(1) 
	passElement = browser.find_element_by_name("mSenha")
	passElement.send_keys(PASS)
	#time.sleep(1)
	passElement.submit()
	return browser

if __name__ == "__main__":
	
	logging.basicConfig(filename='crawler.log',level=logging.INFO)

	browser = login()

	ws = session.query(Weather_station).all()

	for w in ws:

		logging.info('%s (%s): Crawling... ' %(w.omm,w.name))

		start = "01/01/1961" 
		#start = "01/01/2017"  
		end = datetime.now() - timedelta(days=90) # ULTIMOS 90 DIAS ainda NAO estao disponiveis
		end = end.strftime("%d/%m/%Y")
		code_ws = str(w.omm)
		#end = "01/09/2017" 

		url = "http://www.inmet.gov.br/projetos/rede/pesquisa/gera_serie_txt.php?&mRelEstacao="+code_ws+"&btnProcesso=serie&mRelDtInicio="+start+"&mRelDtFim="+end+"&mAtributos=1,1,,,1,1,,1,1,,,1,,,,,"

		browser.get(url)
		soup = BeautifulSoup(browser.page_source,"html.parser")

		try:
			for pre in soup.find('pre'):

				rows = pre.string.splitlines()

				for r in rows:
					if r.startswith(code_ws):

						try:
							dt = datestring_to_date(r.split(';')[1])
						except ValueError:
							dt = None

						try:
							hour_utc = r.split(';')[2]
							hour =  int(int(hour_utc)/100)
							#print hora_utc
							hour_utc_td = timedelta(hours = hour)
							#print hora_utc_td
						except ValueError:
							hour_utc_td = None

						#try:
						hour_utc = r.split(';')[2]
						hour =  int(int(hour_utc)/100)
						dt_complete = datetime(year=dt.year, month=dt.month, day=dt.day, hour=hour)
						#except:
							#dt_complete = None

						try:
							db = float(r.split(';')[3])
						except ValueError:
							db = None

						try:
							wb = float(r.split(';')[4])
						except ValueError:
							wb = None

						try:
							h = float(r.split(';')[5])
						except ValueError:
							h = None

						try:
							p = float(r.split(';')[6])
						except ValueError:
							p = None

						try:
							wd = int(r.split(';')[7])
						except ValueError:
							wd = 0

						try:
							ws = float(r.split(';')[8])
						except ValueError:
							ws = None

						try:
							c = int(r.split(';')[9])
						except ValueError:
							c = None

						try:
							md = Measurements_daily()	
							md.weather_station_id = w.id
							md.measure_date_complete = dt_complete
							md.measure_date = dt
							md.utf_hour = hour_utc_td
							md.temp_dry_bulb = db
							md.temp_wet_bulb = wb
							md.humidity = h
							md.level_pressure_on_station = p
							md.wind_direction = wd
							md.wind_speed =  ws
							md.cloudiness = c

							session.add(md)

						except:
							logging.info(r)
							logging.info(sys.exc_info()[0])

				session.commit()
		
		except TypeError:
			logging.info('%s (%s): End of this stations ...  ' %(w.omm,w.name))
			logging.info('Html:%s' %soup.prettify())

		logging.info('%s (%s): End of this station ...  ' %(w.omm,w.name))




