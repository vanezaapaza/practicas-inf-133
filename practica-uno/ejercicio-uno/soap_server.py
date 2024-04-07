from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def sumar(a, b):
    resultado = a + b
    return "{} + {} = {}".format(a, b, resultado)

def resta(a, b):
    resultado = a - b
    return "{} - {} = {}".format(a, b, resultado)

def multiplicacion(a, b):
    resultado = a * b
    return "{} * {} = {}".format(a, b, resultado)

def division(a, b):
    if b == 0:
        return "No se divide entre cero"
    resultado = a / b
    return "{} / {} = {}".format(a, b, resultado)

dispatcher = SoapDispatcher(
    "soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "Sumar",
    sumar,
    returns={"resultado_suma": str},
    args={"a": int, "b": int},
)

dispatcher.register_function(
    "Restar",
    resta,
    returns={"resultado_resta": str},
    args={"a": int, "b": int},
)

dispatcher.register_function(
    "Multiplicar",
    multiplicacion,
    returns={"resultado_multiplicacion": str},
    args={"a": int, "b": int},
)

dispatcher.register_function(
    "Dividir",
    division,
    returns={"resultado_division": str},
    args={"a": int, "b": int},
)

server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()
