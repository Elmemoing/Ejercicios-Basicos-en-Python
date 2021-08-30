"""
Crear un programa en Python en el que se 
almacenen 3 números en 3 variables A, B y C. El diagrama debe decidir cuál es el mayor y cual es el menor
"""

A = float(input("Ingrese un numero"))
B = float(input("Ingrese otro numero")
C = float(input("Ingrese un tercer numero"))

  def mayor(N1,N2,N3):
          if N1>N2 and N1>N3:
            return N1
          elif N2>N1 and N2>N3:
            return N2
          else
            return N3
          
  def menor(N1,N2,N3):
          if N1<N2 and N1<N3:
            return N1
          elif N2<N1 and N2<N3:
            return N2
          else:
            return N3
          
 Diferentes = A != B and B != C and A != C
          
          if diferentes:
              print("mayor es: ", mayor(A,B,C))
              print("menor es: ", mayor(A,B,C))
          else:
              print("Los numeros deben ser diferentes")
