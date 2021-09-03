#Hacer un programa en Python que lea N 
#números, calcule y escriba la suma de los 
#pares y el producto de los impares

suma_par = 0
mult_impar = 1

total = int(input("Ingrese la cantidad de numeros a calcular:  "))

for i in range(total):
    num = float(input("Ingrese un numero:   "))

    if num % 2 == 0:
        suma_par = suma_par + num
    else:
        mult_impar = mult_impar * num
    
print("La suma de los pares es:   ",suma_par)
print("La multiplicacion de los impares es:   ",mult_impar)

