import json


def WriteToJson(dictionary: dict):
    current_json = ReadJson()

    with open('statistic1.json', 'w') as file:
        current_json["items"].append(dictionary)
        json.dump(current_json, file, indent=4)

def ReadJson():

    with open('statistic1.json', 'r') as file:
        current_json = json.load(file)

    return current_json

def ClearJson():

    current_json = ReadJson()
    current_json['items'] = list()

    with open('statistic1.json', 'w') as file:
        json.dump(current_json, file, indent=4)
