#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cherrypy
import csv
import os
import requests
from model import get_average_temp, generate_forecast_dates, generate_forecast_plot


        
class App(object):

    def __init__(self):
        self.DEFAULT_CITY = "miami"
        self.DEFAULT_COUNTRY = "us"
        self.DEFAULT_DAYS = 7

        self.CITY_LIST_PATH = "C:\\Users\\Phantom\\projects\\ServerStuff\\data\\worldcities.csv"


    
    def city_is_valid(self, input_city):
        """
        Determines the validity of the user input.
        @param input_city: user input
        @return whether the city is a valid city
        """
        data = None
        valid_city = False
        input_city = input_city.title()

        with open(self.CITY_LIST_PATH, 'r', encoding = "utf8") as csv_file:
            data = csv.DictReader(csv_file)
            for row in data:
                if input_city == row["city"]:
                    valid_city = True
                    break

            csv_file.close()
            
        return valid_city

    def country_is_valid(self, country):
        return True

    def num_days_valid(self, days_out):
        return days_out.isnumeric() and int(days_out) > 0 and int(days_out) < 30
    
    @cherrypy.expose
    def weather(self, city, num_days_out):
        city = city if self.city_is_valid(city) else self.DEFAULT_CITY
        
        # country = country if country_is_valid(country) else DEFAULT_COUNTRY

        num_days_out = int(num_days_out) if self.num_days_valid(num_days_out) else self.DEFAULT_DAYS

        query_dict = {"city" : city}

        avg_temps = get_average_temp(query_dict)
        forecast_dates = generate_forecast_dates(num_days_out)
        forecast_html_plot = generate_forecast_plot(forecast_dates, avg_temps, city)
        
        return forecast_html_plot
            
def main():
    config = {
            'global' : {
                'server.socket_host' : '127.0.0.1',
                'server.socket_port' : 8080
            }
        }

    cherrypy.quickstart(App(), '/', config)
        
if __name__ == '__main__':
    main()
    