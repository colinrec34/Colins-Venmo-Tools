import json
import sys

settings_path = sys.path[0] + '/config/settings.json'

with open(settings_path, 'r') as json_file:
    settings = json.load(json_file)

def load_all():
    with open(settings_path, 'r') as json_file:
        return json.load(json_file)

def load_setting(setting):
    with open(settings_path, 'r') as json_file:
        return json.load(json_file)[setting]

def write(setting, value) -> None:
    data = load_all()
    data[setting] = value
    with open(settings_path, 'w') as json_file:
        json.dump(data, json_file)