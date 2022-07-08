#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cherrypy
import csv, os, requests
from src.python.model import get_average_temp

DEFAULT_CITY = "miami"
DEFAULT_COUNTRY = "us"
DEFAULT_DAYS = 7

CITY_LIST_PATH = '../../data/worldcities.csv'

config = {
    'global' : {
        'server.socket_host' : '127.0.0.1',
        'server.socket_port' : 8080
    }
}


def city_is_valid(city):
    # with open(CITY_LIST_PATH, 'r') as csv_file:
    #     data = csv.DictReader(csv_file)

    return False


# function checkCityOrCountry($name)
# {
#     $countries = file_get_contents('https://api.vk.com/method/database.getCities?need_all=1&count=1000&lang=en');
#     $arr = json_decode($countries, true);
#     foreach ($arr['response'] as $country) {
#         if (mb_strtolower($country['title']) === mb_strtolower($name)) {
#             return true;
#         }
#     }

#     return false;

def country_is_valid(country):
    return True

def valid_num_days(days_out):
    return days_out > 0 and days_out < 31


class App(object):
    @cherrypy.expose
    def weather(self, city):
        # city = city if city_is_valid(city) else DEFAULT_CITY
        city = "miami"
        # country = country if country_is_valid(country) else DEFAULT_COUNTRY
        # days_out = days_out if valid_num_days(days_out) else DEFAULT_DAYS

        input_dict = {"city" : city}
        weather_data = get_average_temp(input_dict)
        return f"The average 30 day forecast for {city.title()}: {weather_data}"
            


        
if __name__ == '__main__':
    cherrypy.quickstart(App(), '/', config)