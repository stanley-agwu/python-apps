from bs4 import BeautifulSoup
import requests
import pandas as pd

source= requests.get("https://www.yr.no/place/Nigeria/Lagos/Lagos/long.html").text
soup=BeautifulSoup(source, "lxml")

week_table=soup.find("table", class_="yr-table yr-table-longterm yr-popup-area")

#DATES
week_dates=week_table.find_all("th")
first_day=week_dates[0].text
dates=[th.text for th in week_dates]

#WEATHER CONDITIONS
week_conditions=week_table.find_all("figcaption")
firstDay_conditions=week_conditions[0].text
weather_conditions=[(figcaption).text for figcaption in week_conditions]

#TEMPERATURES
week_temperatures=week_table.find_all(class_="temperature plus")
firstDay_temp=week_temperatures[0].text
temperatures=[(temperature).text for temperature in week_temperatures]

#PRECIPITATIONS
week_precipitations=week_table.find_all("td")
firstDay_precip=week_precipitations[18].text
precipitations=[week_precipitations[i].text for i in range(18, 27)]

#WINDS
try:
    week_winds=week_table.find_all("img")
    firstDay_winds=week_winds[0]["alt"]
    winds=[img["alt"] for img in week_winds]
except Exception as e:
    winds= None

 
weather_forecast = pd.DataFrame(
    {"Dates": dates,
     "Weather Conditions": weather_conditions,
     "Temperatures": temperatures,
     "Precipitations":precipitations,
     "Winds":winds
        })
print(weather_forecast)

weather_forecast.to_csv("weather_forecast.csv")
















