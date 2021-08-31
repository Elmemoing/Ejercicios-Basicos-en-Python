"""
Escribe un programa que pida al usuario el radio de un circulo y calcule su area
sabiendo que: Area = πr2
"""

radio = float(input("ingrese el radio del circulo: "))
pi = 3.1416

area = round(pi * pow(radio,2),2)

print("area del circulo (radio) es: (area) ")
