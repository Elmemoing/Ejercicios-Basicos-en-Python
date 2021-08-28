"""Hacer un programa en Python que permita leer 2 números diferentes
y nos diga cual es el mayor de los 2 números"""

num1 = int(input("Ingrese un numero"))
num2 = int(input("Ingrese otro numero"))

def mayor(a,b):
  if a>b:
    return ("El primer numero es el mayor")
  elif b>a:
    return ("El segundo numero es el mayor")
  else
    returno ("Los numeros son iguales")
   
  print(mayor(num1,num2))
