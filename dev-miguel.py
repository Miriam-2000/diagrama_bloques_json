import json


with open("/home/miguel/diagrama_bloques_json/example_backend.json", "r") as file:
    data = json.load(file)
    print(data)