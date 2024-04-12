import json
from diagrams import Diagram, Cluster, Node


class DiagramNode:

    def __init__(self, id, schemaId, connectedTo):
        self.id = id
        self.schemaId = schemaId
        self.connectedTo = connectedTo


def cargar_datos(data):
    nodos = []
    for item in data:
        nodo = DiagramNode(item['id'],
                           item['schemaId'],
                           item.get('connectedTo', {'inputs': [], 'outputs': []}))
        nodos.append(nodo)
    return nodos


def crear_diagrama(nodos):
    with Diagram("Flujograma", show=False):
        with Cluster("Nodos"):
            nodes = {nodo.id: Node(nodo.schemaId) for nodo in nodos}
            for nodo in nodos:
                for conexion in nodo.connectedTo['outputs']:
                    if conexion in nodes:
                        nodes[nodo.id] >> nodes[conexion]


with open("example_backend.json", "r") as file:
    data = json.load(file)


nodos = cargar_datos(data)
crear_diagrama(nodos)
