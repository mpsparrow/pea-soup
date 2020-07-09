# parsing of config.ini
import configparser

mainConf = "config.ini"

# Reads and returns .ini file
def readINI(filename: str):
    config = configparser.ConfigParser()
    config.read(filename)
    return config

def token():
    conf = readINI(mainConf)
    return conf['Discord']['token']

def defaultPrefix():
    conf = readINI(mainConf)
    return conf['Discord']['defaultPrefix']

def steamKey():
    conf = readINI(mainConf)
    return conf['steamAPI']['key']

def ipKey():
    conf = readINI(mainConf)
    return conf['ipgeolocation']['key']