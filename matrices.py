import os
opciones_mat = ["+","-","*"]
class matrices:
    def __init__(self,filas1,filas2,columnas1,columnas2):
        self.filas1 = filas1
        self.filas2 = filas2
        self.columnas1 = columnas1
        self.columnas2 = columnas2
        self.matriz1 = []
        self.matriz2 = []
        self.matriz3 = []
        self.matriz4 = []
        self.matriz5 = []
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
            return self.matriz3
        else:
            error = print("No se puede realizar la suma porque no son de la misma longitud")
            return error
    def Res_M(self):
        if len(self.matriz1) == len(self.matriz2):
            for i in range(len(self.matriz1)):
                self.matriz3.append((self.matriz1[i] - self.matriz2[i]))
            return self.matriz3
        else:
            error = print("No se puede realizar la resta porque no son de la misma longitud")
            return error
    def Mult_M(self):
        if self.filas1 != self.columnas2:
            error = "Las filas de la matriz 1 y las columnas de la matriz 2 deben de ser iguales para realizar la operacion"
            return error
        else:
            for i in range (self.filas1):
                for j in range (self.columnas2):
                    self.matriz3.append((self.matriz1[j])*(self.matriz2[i]))
            return self.matriz3
def menu_mat ():
    c1 = 1
    c2 = 1
    resultado = matrices(filas1 = int(input("Filas que tendra su matriz #1: ")), columnas1 = int(input("Columnas que tendra su matriz#1: ")), filas2 = int(input("Filas de matriz #2: ")), columnas2 = int(input("Columnas de matriz #2: ")))
    longitud = resultado.filas1*resultado.filas2
    while c1 <= longitud:
        c1 += 1
        m1 = resultado.agregar1(n1=float(input("Valor que desea agregar a matriz 1: ")))
    while c2 <= longitud:
        c2 += 1
        m2 = resultado.agregar2(n2=float(input("Valor que desea agregar a matriz 2: ")))
    opm = input("Operacion a realizar: ")
    if opm not in opciones_mat:
        print("Por favor elija una opcion valida ")
    elif opm == "+":
        m3 = resultado.Sum_M()
        print(m1," + ",m2," = ",m3)
    elif opm == "-":
        m3 = resultado.Res_M()
        print(m1," - ",m2," = ",m3)
    elif opm == "*":
        m3 = resultado.Mult_M()
        print(m1, " * ", m2, " = ", m3)
menu_mat()
