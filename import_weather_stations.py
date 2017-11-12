
import csv

from database import Weather_station
from database import session


def import_weather_stations():
	csvfile  = open('weather_stations.csv', "rt", encoding='utf8')
	text = csv.reader(csvfile, delimiter=',')
	for row in text:
		w = Weather_station()
		w.inmet_id = row[0]
		w.name = row[1]
		w.province = row[2]
		w.omm = row[3]
		session.add(w)
	
	session.commit()

if __name__ == '__main__':
	import_weather_stations()

