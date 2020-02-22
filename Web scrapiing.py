import requests
import pandas as pd
from bs4 import BeautifulSoup

page= requests.get("https://forecast.weather.gov/MapClick.php?lat=42.78489390000004&lon=-112.40271899999999")
soup= BeautifulSoup(page.content, 'html.parser')
week = soup.find(id="seven-day-forecast-body")

items = (week.find_all(class_="tombstone-container"))
#print(items[0])

period = [item.find(class_="period-name").get_text() for item in items]
print(period)
sdes= [des.find(class_="short-desc").get_text() for des in items]
print(sdes)
temperature = [temp.find(class_="temp").get_text() for temp in items]
print(temperature)

weatherStuff= pd.DataFrame({
  "Period":period,
  "Description":sdes,
  "Temperature":temperature
}) 

print(weatherStuff)

weatherStuff.to_csv("datai.csv")
