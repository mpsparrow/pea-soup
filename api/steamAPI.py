# connection to Steam API
import json
import requests
from util import configParse

def getName(steamid: int):
    steamkey = configParse.steamKey()
    url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={steamkey}&format=json&steamids={steamid}"
    response = requests.get(url)
    json = response.json()
    return json['response']['players'][0]['personaname']

def getServers(limit = 500000):
    steamkey = configParse.steamKey()
    url = f"https://api.steampowered.com/IGameServersService/GetServerList/v1/?key={steamkey}&limit={limit}&filter=\appid\420290"
    response = requests.get(url)
    json = response.json()
    return [0]['response']['servers']