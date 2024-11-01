# Iniciamos las variables para la suma y el contador
suma = 0
contador = 0

# Bucle para pedir números hasta que haya un 0
while True:
    numero = float(input("Introduce un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
    contador += 1

# Cálculo de la media
if contador > 0:
    media = suma / contador
    print(f"Suma de todos los números: {suma}")
    print(f"Media de todos los números: {media}")
else:
    print("No se han introducido números.")
