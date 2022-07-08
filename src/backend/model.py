import requests

def kelvin_to_fahrenheit(k):
	return (k - 273.15) * (9/5) + 32

def get_average_temp(input_dict):
    url = "https://community-open-weather-map.p.rapidapi.com/climate/month"

    querystring = {"q":input_dict["city"]}

    headers = {
        "X-RapidAPI-Key": "0ca2611ffbmsh9d5a1de3d8b7c61p13ff7cjsn650876f3c690",
        "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com"
    }
    try:
        response = requests.request("GET", url, headers = headers, params = querystring)
        weather_data = response.json()["list"]
    except Exception as e:
        raise e
    
    average_temps = []
    for i in range(len(weather_data)):
        
        temp_in_fahrenheit = kelvin_to_fahrenheit(weather_data[i]["temp"]["average"])
        average_temps.append(int(temp_in_fahrenheit))

    return str(average_temps)
