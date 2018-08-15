
import csv

from database import Wind_direction
from database import session


def import_wind_directions():
	print("Importando dados wind.")
	csvfile  = open('./data/wind_directions_codes.csv', "rt", encoding='utf8')

	text = csv.reader(csvfile, delimiter=',')
	for row in text:
		wd = Wind_direction()
		wd.id = row[0]
		wd.description = row[1]
		wd.initials = row[2]

		session.add(wd)
	
	session.commit()
	print("Finalizado importados de dados weather.")

if __name__ == '__main__':
	import_wind_directions()