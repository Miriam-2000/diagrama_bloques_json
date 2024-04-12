import json
from diagrams import Diagram, Cluster, Node


class DiagramNode:
    """Representa un nodo en el flujograma
    """
    def __init__(self, id, schemaId, connectedTo):
        """Inicializa un objetos DiagramNode que contiene los datos de un nodo

        Args:
            id (str): Identificación del nodo.
            schemaId (str): Nombre del nodo.
            connectedTo (_type_): Conexiones del nodo con otros.
        """
        self.id = id
        self.schemaId = schemaId
        self.connectedTo = connectedTo


def cargar_datos(data):
    """Genera una lista que contiene las instacias de cada objeto que corresponde a un nodo

    Args:
        data (List): Lista de diccionarios que contiene los datos

    Returns:
        list: Lista con los nodos (objetos)
    """
    nodos = []
    for item in data:
        nodo = DiagramNode(item['id'],
                           item['schemaId'],
                           item.get('connectedTo', {'inputs': [], 'outputs': []}))
        nodos.append(nodo)
    return nodos


def crear_diagrama(nodos):
    """Crea el flujograma a partir de los nodos y sus respectivas conexiones

    Args:
        nodos (List): Lista con los nodos (objetos)
    """
    # Inicializa un nuevo diagrama (Diagram)
    with Diagram("Flujograma", show=False):
        # Agrupa todos los nodos relacionados (Cluster), en este caso todos
        with Cluster("Nodos"):
            # Se crean los nodos (Node) --> (Node = ID + Nombre)
            nodes = {nodo.id: Node(nodo.schemaId) for nodo in nodos}
            # Crea las conexiones comparando las salidas con el ID del nodo
            for nodo in nodos:
                for conexion in nodo.connectedTo['outputs']:
                    if conexion in nodes:
                        nodes[nodo.id] >> nodes[conexion]


with open("example_backend.json", "r") as file:
    data = json.load(file)

nodos = cargar_datos(data)
crear_diagrama(nodos)
