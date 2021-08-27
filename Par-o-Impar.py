#Desarrolle un programa en Python que permita leer un valor cualquiera N y escriba si dicho número es par o impar

num = int(input("Ingrese un numero"))

def par_impar(n):
  if n/2 == 0:
      return("El numero es Par")
  else:
      return("El numero es impar")
  
  print(par_Impar(num))
