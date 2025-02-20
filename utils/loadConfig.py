import json

def loadConfig():
    with open("config.json", "r") as configFile:
        return json.load(configFile)