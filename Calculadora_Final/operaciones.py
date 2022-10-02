import matrices as m
opciones_n = ["+", "-", "*", "/","M", "Q"]
class operaciones_norm:
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
def menu_principal ():
    print("""    Suma            +
    Resta           -
    Multiplicacion  *
    Division        /
    Matrices        M
    Salir           Q""")
    opcion = input("---> ").upper()
    return opcion
while True:
    op = menu_principal()
    if op not in opciones_n:
        print("Introduzca una operacion valida por favor.")
    elif op == "Q":
        print("Gracias por utilizar esta calculadora")
        exit(0)
    elif op == "M":
        m.menu_mat()
    else:
        n1 = float(input("Introduzca el primer numero "))
        n2 = float(input("Introduzca el segundo numero "))
        if op == "+":
            resultado = operaciones_norm(n1, n2)
            print(n1, op, n2, " = ",resultado.sumas())
        elif op == "-":
            resultado = operaciones_norm(n1, n2)
            print(n1, op, n2, " = ",resultado.restas())
        elif op == "*":
            resultado = operaciones_norm(n1, n2)
            print(n1, op, n2, " = ",resultado.multiplicacion())
        elif op == "/":
            resultado = operaciones_norm(n1, n2)
            if n2 == 0:
                print("Cualquier numero entre 0 es indefinido")
            else:
                print(n1, op, n2, " = ",resultado.division())