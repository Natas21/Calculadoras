import os
import readchar

print("Esta es una calculadora para operaciones basicas con dos numeros\n")
endprogram = False
#Ciclo while "infinito" para que se repita el progama siempre y cuando no lo quieras cerrar
while not endprogram:
    #Preguntamos la operacion a realizar y utilizamos readchar para no tener que presionar enter cada vez que queramos elegir una operacion.
    print("""Por favor, indique que operacion realizara:\n
                 Salir [Q]\n
                 Suma [S]\n
                 Resta [R]\n
                 Multiplicacion [X]\n
                 Division [D]\n
                 Matrices [M]""")
    operacion = readchar.readchar()
    #Suma de dos numeros
    if operacion=="S" or operacion=="s":
        os.system("cls")
        suma1 = float(input("""Introduzca el primer sumando """))
        suma2 = float(input("""Introduzca el segundo sumando """))
        sumas = suma1 + suma2
        print("El resultado de su suma es: {}".format(sumas))
    #Resta de dos numeros
    elif operacion=="R" or operacion=="r":
        os.system("cls")
        resta1 = float(input("""Introduzca el primer numero """))
        resta2 = float(input("""Introduzca el segundo numero """))
        restas = resta1 - resta2
        print("El resultado de su resta es: {}".format(restas))
    #Multiplicacion de dos numeros
    elif operacion=="X" or operacion=="x":
        os.system("cls")
        multi1 = float(input("""Introduzca el primer termino """))
        multi2 = float(input("""Introduzca el segundo termino """))
        multis = multi1 * multi2
        print("El resultado de su suma es: {}".format(multis))
    #Division de dos numeros
    elif operacion=="D" or operacion=="d":
        os.system("cls")
        divi1 = float(input("""Introduzca el dividendo """))
        divi2 = float(input("""Introduzca el divisor """))
        #endprogram = false para que nos regrese al inicio en lugar de permitir que se ejecute un error
        if divi2 == 0:
            print("Por favor introduzca un valor distinto de 0")
            endprogram = False
        else:
            divis = divi1 / divi2
            print("El resultado de su resta es: {}".format(divis))
    #Crear y operar con matrices
    if operacion =="M" or operacion =="m":
        for matrices in range(0,1):
            #Declaracion de matriz
            filas1 = int(input("Cantidad de filas: "))
            columnas1 = int(input("Cantidad de columnas: "))
            matriz1 = []
            # Creacion de matriz
            for f in range(filas1):
                matriz1.append([])
                # Introducir valores a matriz
                for c in range(columnas1):
                    valor = float(input("Elemento %d,%d: " % (f + 1, c + 1)))
                    matriz1[f].append(valor)
            # Mostrar matriz en pantalla (consola)
            print()
            for fila in matriz1:
                print("[", end=" ")
                for elemento in fila:
                    print("{:8.2f}".format(elemento), end=" ")
                print("]")
            print()
        for matrices in range(0,1):
            #Declaracion de matriz
            filas2 = int(input("Cantidad de filas: "))
            columnas2 = int(input("Cantidad de columnas: "))
            matriz2 = []
            # Creacion de matriz
            for f in range(filas2):
                matriz2.append([])
                # Introducir valores a matriz
                for c in range(columnas2):
                    valor = float(input("Elemento %d,%d: " % (f + 1, c + 1)))
                    matriz2[f].append(valor)
            # Mostrar matriz en pantalla (consola)
            print()
            for fila in matriz2:
                print("[", end=" ")
                for elemento in fila:
                    print("{:8.2f}".format(elemento), end=" ")
                print("]")
            print()
            #Preguntamos la operacion que realizaremos a la matriz
            print("""Por favor, indique que operacion realizara a las matrices:\n
                             Salir [Q]\n
                             Suma [S]\n
                             Resta [R]\n
                             Multiplicacion [X]\n""")
            o_matriz = readchar.readchar()
            #Suma de dos matrices
            if o_matriz == "S" or o_matriz == "s":
                os.system("cls")
                def sumar_matrices (matriz1, matriz2):
                    if len(matriz1) == len(matriz2) and len(matriz1[0]) == len(matriz2[0]):
                        matriz3 = []
                        for f in range(len(matriz1)):
                            matriz3.append([])
                            for c in range (len(matriz1[0])):
                                matriz3[f].append(matriz1[f][c] + matriz2 [f][c])
                        return matriz3
                    else:
                        return None
                resultado = sumar_matrices(matriz1,matriz2)
                if resultado == None:
                    print("No se pueden sumar porque no son de las mismas filas y columnas")
                else:
                    print("El resultado de sumar ambas matrices es:\n")
                    for fila in resultado:
                        print("[", end=" ")
                        for elemento in fila:
                            print(elemento, end=" ")
                        print("]")
            #Resta de matrices
            elif o_matriz == "R" or o_matriz == "r":
                os.system("cls")
                def restar_matrices(matriz1, matriz2):
                    if len(matriz1) == len(matriz2) and len(matriz1[0]) == len(matriz2[0]):
                        matriz3 = []
                        for f in range(len(matriz1)):
                            matriz3.append([])
                            for c in range(len(matriz1[0])):
                                matriz3[f].append(matriz1[f][c] - matriz2[f][c])
                        return matriz3
                    else:
                        return None
                resultado = restar_matrices(matriz1, matriz2)
                if resultado == None:
                    print("No se pueden restar porque no son de las mismas filas y columnas")
                else:
                    print("El resultado de restar ambas matrices es:\n")
                    for fila in resultado:
                        print("[", end=" ")
                        for elemento in fila:
                            print(elemento, end=" ")
                        print("]")
            #Multiplicacion de matrices
            elif o_matriz == "X" or o_matriz == "x":
                os.system("cls")
                def multiplicar_matrices (matriz1, matriz2):
                    if len(matriz1[0]) == len(matriz2):
                        matriz3 = []
                        for f in range(len(matriz1)):
                            matriz3.append([])
                            for c in range (len(matriz2[0])):
                                matriz3[f].append(0)
                        for f in range(len(matriz1)):
                            for c in range(len(matriz2[0])):
                                for k in range(len(matriz1[0])):
                                    matriz3 [f][c] += matriz1 [f][k] * matriz2 [k][c]
                        return matriz3
                    else:
                        return None
                resultado = multiplicar_matrices(matriz1,matriz2)
                if resultado == None:
                    print("No se pueden multiplicar porque no son de las mismas filas que columnas")
                else:
                    print("El resultado de multiplicar ambas matrices es:\n")
                    for fila in resultado:
                        print("[", end=" ")
                        for elemento in fila:
                            print(elemento, end=" ")
                        print("]")
    #Salir del programa
    elif operacion =="Q" or operacion == "q":
        endprogram = True
        os.system("cls")
        print("Gracias por usar esta calculadora")
        exit()
