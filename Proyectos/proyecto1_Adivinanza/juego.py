import random

def adivinanza():
    # Generamos un número del 1 al 100
    SecretNumber = random.randint(1, 100)
    intentos = 0

    # Damos la bienvenida
    print('Bienvenido al juego de adivinanza')
    print('Debes adivinar un número del 1 al 100')
    print('¡Intenta adivinarlo!')

    while True:
        adivinanza = input('Introduce un número del 1 al 100: ')

        # Verificamos que sea un número
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # De str a int
            intentos += 1

            if adivinanza < SecretNumber:
                print(f'El número secreto es mayor que: {adivinanza}')
            elif adivinanza > SecretNumber:
                print(f'El número secreto es menor que: {adivinanza}')
            else:
                print(f'¡Has ganado! El número {adivinanza} es el secreto y lo has logrado en {intentos} intentos.')
                break  # Salimos del bucle al adivinar correctamente
        else:   
            print('Por favor, introduce un número válido.')

adivinanza()

