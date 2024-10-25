#Escribe una función en Python que procese una lista de cadenas de texto y realice las siguientes acciones:
#Tomar una lista de frases y convertir cada frase en una lista de palabras.
#Luego, debe crear una nueva lista que contenga la cantidad de palabras en cada frase.
#Tambien debe crear un lista que contenga la cantidad de caracteres en cada frase.
#Finalmente, debe imprimir cada frase original junto con la cantidad de palabras que contiene

def convertirFrase(listado):
    for frase in listado:
        totalPalabra = frase.split()
        
        palabras = len(totalPalabra)  # Número de palabras
        letras = sum(len(palabra) for palabra in totalPalabra) # Almacena el total de letras en todas las palabras

        print('Frase:', frase)
        print('Número de palabras:', palabras)
        print('Número de letras:', letras)
        print()


lista = [
    'La utn es una mierda',
    'Dk de mi vida'
]

#convertirFrase(lista)  


# Ejercicio 2
# Escribe un programa que reciba un número entero y determinar si es par o impar

def esPar(numero):
    numero = int(numero)

    return 'El número es par' if numero % 2 == 0 else 'El número es impar'

print(esPar(3))