"""
Crear un programa en Python para sumar 10 números leídos por teclado
"""

suma = 0

for i in range(10):
  numero = int(input("ingrese un numero"))
  suma = suma + numero
  
  print("la suma es: ", suma)
