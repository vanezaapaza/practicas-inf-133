import requests
# Consultando a un servidor RESTful
url = "http://localhost:8000/"

# Agregando un nuevo paciente
ruta_post = url + "pacientes"
nuevo_paciente = {
    "ci": 123456789,
    "nombre": "María",
    "apellido": "González",
    "edad": 30,
    "genero": "femenino",
    "diagnostico": "asma",
    "doctor": "Zofia",
}
post_response = requests.post(url=ruta_post, json=nuevo_paciente)
print(post_response.text)

# Obteniendo todos los pacientes
ruta_get = url + "pacientes"
get_response = requests.get(url=ruta_get)
print(get_response.text)

# Obteniendo paciente por CI
ci = 9943299
ruta_get_ci = f"{url}pacientes/{ci}"
get_response_ci = requests.get(url=ruta_get_ci)
print(get_response_ci.text)

# Filtrando pacientes por diagnóstico
diagnostico = "asma"
ruta_get_diagnostico = f"{url}pacientes/?diagnostico={diagnostico}"
get_response_diagnostico = requests.get(url=ruta_get_diagnostico)
print(get_response_diagnostico.text)

# Filtrando pacientes por doctor
doctor = "Zofia"
ruta_get_doctor = f"{url}pacientes_doc/?doctor={doctor}"
get_response_doctor = requests.get(url=ruta_get_doctor)
print(get_response_doctor.text)

# Actualizando paciente
ci_update = 123456789
ruta_put = f"{url}pacientes/{ci_update}"
paciente_actualizado = {
    "ci": ci_update,
    "nombre": "María",
    "apellido": "González",
    "edad": 35,
    "genero": "femenino",
    "diagnostico": "asma",
    "doctor": "Edriel",
}
put_response = requests.put(url=ruta_put, json=paciente_actualizado)
print(put_response.text)

# Eliminando pacientes
ruta_del = url + "pacientes"
delete_response = requests.delete(url=ruta_del)
print(delete_response.text)
