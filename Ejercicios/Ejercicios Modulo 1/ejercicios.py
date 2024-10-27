# 1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def max(n1 , n2):
    if n1 >= n2:
        print(f'El número 1: {n1} es mayor a número 2: {n2}')
    elif n2 <= n1:
        print(f'El número 2: {n2} es menor a número 1: {n1}')
    else:
        print(f'Los números {n1} y {n2} son iguales')

#max(9 , 5)
#max(5 , 10)
#max(5 , 5)

###############################################################

# 2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def max_de_tres(n1 , n2 , n3):
    if n1 > n2 and n1 > n3:
        print(f'El primer número {n1} es mayor a {n2} y {n3}')
    elif n2 > n1 and n2 > n3:
        print(f'El segundo número {n2} es mayor a {n1} y {n3}')
    elif n3 > n1 and n3 > n2:
        print(f'El tercer número {n3} es mayor a {n1} y {n2}')

#max_de_tres(n1 = 23 , n2 = 15 , n3 = 10)

################################################################

# 3 - Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

def calc_long(elemento):
    count = 0
    
     # Verifca si un objeto es una instancia
    if isinstance(elemento , (str , list)):
        for _ in elemento:
            count += 1
    else:
        return 'Entrada no válida , proporcione una lista por favor'
    
    return count


cadenaPrueba = 'HolaMundo'
listaPrueba = [1,2,3,4,5]
listaVacia = []

print(calc_long(cadenaPrueba))
print(calc_long(listaPrueba))

############################################################

# 4-
