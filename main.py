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
            item['id'], 
            item['schemaId'],
            item.get('connectedTo', {'input': [], 'output': []})
        )
    nodos.append(nodo)
    print(nodos)
    return nodos





with open("example_backend.json", "r") as file:
    data = json.load(file)



cargar_datos(data)
