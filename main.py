
'''
Hasta ahora hemos
trabajado con variables
que permiten almacenar
un único valor
'''



edad = 16

altura = 1.70

nombre = "Maritza"

estado = True

'''
En python podemos
usar las variables 
que almacenes una
colección de datos
y luego accederla
usando un subindice
'''

# lista de enteros
lista1 = [10, 5, 3, 9]
# lista de decimales
lista2 = [1.78, 2.66, 1.55, 89.4, 6.9]
#lista de string
lista3 = ["Lunes","Mates","Miercoles"]

'''
Lista de elemetos
de distinto tipo  
'''

lista4 = ["Maritza", 45, 1.92, False]


if __name__ == '__main__':

    '''
    Cantidad de elementos de cada lista
    '''
    print(len(lista1))
    print(len(lista2))
    print(len(lista3))
    print(len(lista4))

    print()
    print(lista1)
    lista1[3] = 23
    print()
    print(lista1)

    lista1[2] = 4
    print()
    print(lista1)