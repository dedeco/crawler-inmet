from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Weather_station(Base):
	__tablename__ = 'weather_stations'
	id = Column(Integer(), primary_key = True)
	inmet_id = Column(Integer())
	name = Column(String(255),)
	province = Column(String(2),)
	omm = Column(Integer())

class Measurements_daily(Base):
	__tablename__ = 'measurements_daily'
	id = Column(Integer(), primary_key = True)
	weather_station_id = Column(Integer(), ForeignKey('weather_stations.id'), nullable=False)
	measure_date_complete = Column(DateTime())
	measure_date =  Column(Date())
	utf_hour = Column(Interval())
	temp_dry_bulb = Column(Float())
	temp_wet_bulb  = Column(Float())
	humidity  = Column(Float())
	level_pressure_on_station  = Column(Float())
	wind_direction = Column(Integer(), ForeignKey('wind_directions.id'), nullable=False)
	wind_speed  = Column(Float())
	cloudiness  = Column(Float())

	Weather_Station = relationship("Weather_station", lazy='joined')
	Wind = relationship("Wind_direction", lazy='joined')

class Wind_direction(Base):
	__tablename__ = 'wind_directions'
	id =Column(Integer(),primary_key = True)
	description = Column(String(32),)
	initials = Column(String(5),)