import random 

# Función para obtener una palabra aleatoria
def obtener_palabra():
    palabras = ['Python', 'JavaScript', 'Angular', 'React', 'Git', 'Flask']  # Lista de palabras posibles.
    return random.choice(palabras)  # Selecciona y devuelve una palabra aleatoria de la lista.

# Función para mostrar el progreso de la palabra adivinada
def mostrar_progreso(palabra_secreta, letras_adivinadas):
    progreso = ''  # Inicializa una cadena vacía que contendrá el progreso de la palabra.
    for letra in palabra_secreta:  # Recorre cada letra de la palabra secreta.
        if letra in letras_adivinadas: # Si la letra se adivino
            progreso += letra  
        else:
            progreso += '_'  # Si no, agrega un guion bajo en lugar de la letra.
    return progreso  # Devuelve la palabra mostrando solo las letras adivinadas y el resto como guiones.

# Función principal del juego de ahorcado
def juego_ahorcado():
    palabra_secreta = obtener_palabra()  # Selecciona una palabra secreta al azar.
    letras_adivinadas = []  # Lista vacía para almacenar las letras que el jugador ha adivinado.
    intentos = 6  # Número de intentos permitidos.
    juego_terminado = False  # Bandera para saber si el juego ha terminado.


    print('Bienvenido al juego del ahorcado')
    print(f'Tienes {intentos} intentos para adivinar la palabra secreta.')
    print(mostrar_progreso(palabra_secreta, letras_adivinadas))  # Muestra el estado inicial de la palabra.

    # Ciclo principal del juego
    while not juego_terminado and intentos > 0:  # El juego continúa mientras no haya terminado y queden intentos.
        letra = input('Introduce una letra: ').lower()  # Pide una letra al jugador y la convierte a minúscula.

        # Validación de la entrada del jugador
        if len(letra) != 1 or not letra.isalpha():  # Verifica si la entrada es una letra válida.
            print('Por favor, introduce una letra válida.')
        elif letra in letras_adivinadas:  # Si la letra ya fue adivinada anteriormente...
            print('Ya has utilizado esa letra, prueba con otra.')
        else:
            letras_adivinadas.append(letra)  # Añade la letra a la lista de letras adivinadas.

            if letra in palabra_secreta:  # Si la letra está en la palabra secreta...
                print(f'¡Muy bien! La letra {letra} está presente en la palabra.')
            else:  # Si la letra no está en la palabra secreta...
                intentos -= 1  # Se resta un intento.
                print(f'Lo siento, la letra {letra} no está en la palabra secreta.')
                print(f'Te quedan {intentos} intentos.')  # Informa cuántos intentos quedan.

            progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)  # Actualiza y muestra el progreso.
            print(progreso_actual)

            # Verifica si el jugador ha ganado (todas las letras fueron adivinadas)
            if "_" not in progreso_actual:
                juego_terminado = True  # Termina el juego.
                print(f'¡Has ganado! Felicitaciones. La palabra secreta es: {palabra_secreta}.')
            
            # Verifica si el jugador ha perdido (se acabaron los intentos)
            if intentos == 0:
                print(f'Se te han acabado los intentos. La palabra secreta era: {palabra_secreta}.')


juego_ahorcado()
