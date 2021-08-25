#Hacer un programa para sumar dos números leídos por teclado y escribir el resultado

numero_uno = int(input("Ingrese un numero"))
numero_dos = int(input("Ingrese otro numero"))

def suma(a,b):
  suma = (a+b)
  return suma

print(suma(numero_uno,numero_dos))
