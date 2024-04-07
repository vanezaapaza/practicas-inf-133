import requests

# Definir la URL del servidor GraphQL
url = "http://localhost:8000/graphql"

# Definir la consulta GraphQL para crear una nueva planta
query_crear = """
mutation {
        crearPlanta(nombre: "manzano", especie: "Malus domestica", edad: 25 ,altura: 300, frutos:"True") {planta {id nombre especie edad altura frutos}}
        }"""

response_creacion = requests.post(url, json={"query": query_crear})
# Creación de planta
print(response_creacion.text)

# Definir la consulta GraphQL para obtener una lista de plantas
query_lista = """{
        plantas{id nombre especie edad altura frutos}
        }"""

response_lista = requests.post(url, json={"query": query_lista})
# Listado de plantas
print(response_lista.text)

# Definir la consulta GraphQL con parámetros para buscar plantas por especie
query_especie = """{
        plantaPorEspecie(especie: "Malus domestica"){id nombre especie edad altura frutos}
        }"""

response_especie = requests.post(url, json={"query": query_especie})
# Buscar plantas por especie
print(response_especie.text)

# Definir la consulta GraphQL con parámetros para buscar plantas por fruta
query_fruta = """{
        plantaPorFruta(frutos: "True"){id nombre especie edad altura frutos}
        }"""

response_fruta = requests.post(url, json={"query": query_fruta})
# Buscar plantas por fruta
print(response_fruta.text)

# Definir la consulta GraphQL para actualizar una planta
query_actualizar = """mutation {actualizarPlanta(id: 1 ,nombre: "margarita", especie: "Bellis perennis", edad: 24 ,altura: 10, frutos:"False") {planta {id nombre especie edad altura frutos}}
        }"""

response_actualizar = requests.post(url, json={"query": query_actualizar})
# Actualización de planta
print(response_actualizar.text)

# Definir la consulta GraphQL para eliminar una planta
query_eliminar = """mutation {deletePlanta(id: 3){planta {id nombre especie edad altura frutos}}
        }"""

response_eliminar = requests.post(url, json={"query": query_eliminar})
# Eliminación de planta
print(response_eliminar.text)

# Definir nuevamente la consulta GraphQL para obtener una lista de plantas
query_lista = """{plantas{id nombre especie edad altura frutos}}"""

response_lista_actualizada = requests.post(url, json={"query": query_lista})
# Listado de plantas actualizado
print(response_lista_actualizada.text)
