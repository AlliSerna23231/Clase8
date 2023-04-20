def sumar_5_enteros():
    # definimos las variables
    lista = []
    contadorWhile = 0
    tamano = 5
    suma = 0

    # Ingresamos los números
    while contadorWhile < tamano:
        lista.append(int(input("Ingrese números " + str(contadorWhile+1) + ": ")))
        contadorWhile += 1

    # suma los números
    contadorWhile = 0
    while contadorWhile < tamano:
            suma += lista[contadorWhile]
            contadorWhile += 1

    print("Los elementos de la lista son:")
    for numero in lista:
        print(numero, end=', ')

    print("\nLa suma de todos sus elementos es:")
    print(suma)


