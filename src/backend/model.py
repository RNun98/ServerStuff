import requests
import os
import plotly
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import pandas as pd

from datetime import datetime, date, timedelta
    
def kelvin_to_fahrenheit(k):
    """
    Converts kelvin to fahrenheit.
    @param k: temp in kelvin.
    @return temp in fahrenheit
    """
    return (k - 273.15) * (9/5) + 32

def get_average_temp(input_dict):
    """
    Function to get the average temp of a valid city.
    @param input_dict: Dictionary that contains the average weather data for a given city.
    @return a list of the average temperatures for 30 days in the future
    """
    url = "https://community-open-weahter-map.p.rapidapi.com/climate/month"
    city = input_dict["city"]
    
    # Quering the weather api for the city specific data
    querystring = {"q" : city}

    headers = {
        "X-RapidAPI-Key": "0ca2611ffbmsh9d5a1de3d8b7c61p13ff7cjsn650876f3c690",
        "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com"
    }
    
    try:
        # Getting weather data
        response = requests.request("GET", url, headers = headers, params = querystring)
        weather_data = response.json()["list"]
    except Exception as e:
        raise e
    
    average_temps_list = []
    for i in range(len(weather_data)):
        temp_in_fahrenheit = kelvin_to_fahrenheit(weather_data[i]["temp"]["average"])
        average_temps_list.append(int(temp_in_fahrenheit))

    return average_temps_list

def generate_forecast_plot(dates, avg_temps, city):
    """
    Generates the line graph for the average temperature data.
    Los Angeles_firstDate_lastDate.html
    @param dates: the forecast dates list
    @param avg_temps: a list of the average temperatures for a city
    @param city: the city that the data is being gathered for
    @return the html file that contains the graph
    """
    FILE_NAME = f"{city.title()}_{dates[0]}_{dates[len(dates) - 1]}_average_temps.html"
    GRAPH_HTML = f"C:\\Users\\Phantom\\projects\\ServerStuff\\src\\frontend\\average_temp_graphs"
    GRAPH_PATH = os.path.join(GRAPH_HTML, FILE_NAME)
        
    # Create a trace
    data = [go.Scatter(
        x = dates,
        y = avg_temps,
    )]

    # Create a layout
    layout = go.Layout(
            xaxis=dict(
                title = "Forecast Dates",    
            ),
            yaxis=dict(
                title = f"Average temperatures for {city.title()}",  
            )
        )

    # Create the graph and write it to an html file
    fig = go.Figure(data = data, layout = layout)
    fig.write_html(GRAPH_PATH)

    return open(GRAPH_PATH)

def generate_forecast_dates(num_days_out = 30):
    """
    Returns the dates of the next num_days_out.
    @param num_days_out: how many days to look ahead
    @return The next num_days_out dates
    """    
    current_date = date.today()

    forecast_dates = []
    for _ in range(num_days_out):
        # Getting the next day
        current_date += timedelta(days = 1)
        forecast_dates.append(current_date)

    return forecast_dates