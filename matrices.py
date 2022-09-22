import os
import readchar

c1=1
c2=1
class matrices:
    def __init__(self,longitud):
        self.largo = longitud
        self.matriz1 = []
        self.matriz2 = []
        self.matriz3 = []
    def agregar1 (self, n1):
        self.matriz1.append(n1)
        return self.matriz1
    def agregar2 (self, n2):
        self.matriz2.append(n2)
        return self.matriz2
    def Sum_M (self):
        if len(self.matriz1) == len(self.matriz2):
            for i in range(len(self.matriz1)):
                self.matriz3.append((self.matriz1[i] + self.matriz2[i]))
            print(self.matriz3)
            return self.matriz3
        else:
            error = print("No se puede realizar la suma porque no son de la misma longitud")
            return error

filas1 = int(input("Filas que tendra su matriz: "))
columnas1 = int(input("Columnas que tendra su matriz: "))
longitud = filas1 * columnas1
resultado = matrices(longitud)
while c1 <= longitud:
    c1 += 1
    m1 = resultado.agregar1(n1= float(input("Valor que desea agregar: ")))
filas2 = int(input("Filas que tendra su matriz: "))
columnas2 = int(input("Columnas que tendra su matriz: "))
longitud = filas2*columnas2
resultado2 = matrices(longitud)
while c2 <= longitud:
    c2 +=1
    m2 = resultado.agregar2(n2=float(input("Valor que desea agregar: ")))
longitud3 = longitud
resultado3 = matrices(longitud3)
m3 = resultado.Sum_M()
print(m1,m2,m3)
