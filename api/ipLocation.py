# gets location of IP address (for server location)
import json
import requests
from util import configParse

def locate(ip: str):
    key = configParse.ipKey()
    url = f"https://api.ipgeolocation.io/ipgeo?apiKey={key}&ip={ip}"
    response = requests.get(url)
    json = response.json()
    return ['continent_name']