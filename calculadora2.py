import os
opciones = ["+", "-", "*", "/", "Q"]
matriz = []
class matrices:
    def __init__(self,longitud):
        self.largo = longitud
        self.matriz = []
    def agregar (self, n):
        self.matriz.append(n)
        return self.matriz
class operaciones:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    def sumas (self):
        return self.n1 + self.n2
    def restas (self):
        return self.n1 - self.n2
    def multiplicacion (self):
        return self.n1 * self.n2
    def division (self):
        return self.n1 / self.n2
def menu ():
    print("""    Suma            +
    Resta           -
    Multiplicacion  *
    Division        /
    Salir = [Q]""")
    opcion = input("---> ").upper()
    return opcion
while True:
    op = menu()
    if op not in opciones:
        os.system("cls")
        print("Introduzca una operacion valida por favor.")
    elif op == "Q":
        print("Gracias por utilizar esta calculadora")
        break
    else:
        n1 = float(input("Introduzca el primer numero "))
        n2 = float(input("Introduzca el segundo numero "))
        if op == "+":
            os.system("cls")
            resultado = operaciones(n1, n2)
            print(n1, op, n2, " = ",resultado.sumas())
        elif op == "-":
            os.system("cls")
            resultado = operaciones(n1, n2)
            print(n1, op, n2, " = ",resultado.restas())
        elif op == "*":
            os.system("cls")
            resultado = operaciones(n1, n2)
            print(n1, op, n2, " = ",resultado.multiplicacion())
        elif op == "/":
            os.system("cls")
            resultado = operaciones(n1, n2)
            if n2 == 0:
                print("Cualquier numero entre 0 es indefinido")
            else:
                print(n1, op, n2, " = ",resultado.division())
        elif op == "M":
            filas = int(input("Filas que tendra su matriz: "))
            columnas = int(input("Columnas que tendra su matriz: "))
            longitud = filas * columnas
            resultado = matrices(longitud)
            i = 0
            while i <= longitud:
                i += 1
                m = resultado.agregar(n=float(input("Valor que desea agregar: ")))
                print(m)
