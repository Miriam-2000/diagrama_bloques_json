import json


with open("/home/miguel/diagrama_bloques_json/example_backend.json", "r") as file:
    data = json.load(file)

datos = []
for item in data:
    dato = {
        "id": item['id'],
        "schemaId": item['schemaId'],
        "connectedTo": item['connectedTo']
    }
    datos.append(dato)

print(datos)
