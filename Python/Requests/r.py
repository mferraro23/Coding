import requests
from bs4 import BeautifulSoup
import os
import sys

url = "https://food.google.com/chooseprovider?restaurantId=/g/1tdb9rvg&g2lbs=ALgbXSodGcc9p16nRqwXCw21vNFLsSrWMEN0TTAx_qBLuYtzgw0MKI-yhqzFBdus6IkomgQls8DW&hl=en-US&gl=us&cs=1&ssta=1&fo_m=MfohQo559jFvMWwP9igWZeWQMczq7voErUdXMT_RFPQ05bfKMQVr5-7IofUJMU_hT8vrWuwRMUOzJVpjPL1YMfaXTPp5KXh-OAE%3D&gei=60VwYfWRNYSk_QbE373QDQ&fo_s=OA,AH&orderType=1&sei=Ca-2eFnKDwenEbaKvgFU4bRJ&utm_campaign&utm_source=search"

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

data = []

for div in soup.find_all('div', {'class': 'SUXJqf'}):
    for names in div.find_all('div', {'role': 'tab'}):
        values = names.text.strip()
        data.append(values.lower())
        print(values)

selection = input("What menu category do you want to order from?").lower()

if selection in data:
    print("Okay we are on it!")
 
else:
    print("We cant find what you want!")

