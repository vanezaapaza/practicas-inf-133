from zeep import Client

client = Client('http://localhost:8000')
resultado_suma = client.service.Sumar(a=10, b=5)
resultado_resta = client.service.Restar(a=10, b=5)
resultado_multiplicacion = client.service.Multiplicar(a=10, b=5)
resultado_division = client.service.Dividir(a=10, b=5)

print(resultado_suma)
print(resultado_resta)
print(resultado_multiplicacion)
print(resultado_division)
