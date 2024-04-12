import json


class DiagramNode:

    def __init__(self, id, schemaId, connectedTo):
        self.id = id
        self.schemaId = schemaId
        self.connectedTo = connectedTo

def cargar_datos(data):
    nodos = []

    for item in data:
        nodo = DiagramNode(
            item[id], 
            item['schemaId'],
            item.get['connectedTo'], input = [], output = []
        )
    nodos.append(nodo)

    return nodos


with open("example_backend.json", "r") as file:
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
