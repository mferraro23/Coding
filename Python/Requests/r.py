import requests
from bs4 import BeautifulSoup
import os
import sys

from requests.models import Response

url = "https://food.google.com/chooseprovider?restaurantId=/g/1tdb9rvg&g2lbs=ALgbXSodGcc9p16nRqwXCw21vNFLsSrWMEN0TTAx_qBLuYtzgw0MKI-yhqzFBdus6IkomgQls8DW&hl=en-US&gl=us&cs=1&ssta=1&fo_m=MfohQo559jFvMWwP9igWZeWQMczq7voErUdXMT_RFPQ05bfKMQVr5-7IofUJMU_hT8vrWuwRMUOzJVpjPL1YMfaXTPp5KXh-OAE%3D&gei=60VwYfWRNYSk_QbE373QDQ&fo_s=OA,AH&orderType=1&sei=Ca-2eFnKDwenEbaKvgFU4bRJ&utm_campaign&utm_source=search"

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

data = {}
data2 = []

def find_list(selection):
    indexValue = data.get(selection)
    for div in soup.find_all('div', {'class': 'SUXJqf'}):
        for names in div.find_all('div', {'role': 'tab'}):
            name = names.find(data[indexValue]) 
            print(name)
                


n=1
for div in soup.find_all('div', {'class': 'SUXJqf'}):
    for names in div.find_all('div', {'role': 'tab'}):
        values = names.text.strip()
        data[values.lower()] = n
        data2.append(values)
        print(n, values)
        n+=1

selection = input("What menu category do you want to order from?").lower()

if selection in data:
    print("Okay, we are on it!")
    find_list(selection=selection)
 
else:
    print("We cant find what you want!")

