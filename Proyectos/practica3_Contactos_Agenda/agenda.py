def mostrar_menu():
    # Función que imprime el menú con las opciones disponibles para el usuario
    print('\nAgenda de contactos:')
    print('1. Agregar nuevo contacto')
    print('2. Eliminar contacto existente')
    print('3. Buscar contacto')
    print('4. Lista de contacto')
    print('5. Salir del programa')

def agregar_contacto(agenda):
    # Solicita al usuario los datos del nuevo contacto
    nombre = input('Por favor introducí el nombre completo del contacto:')
    telefono = input('Por favor introducí el teléfono del contacto:')
    email = input('Por favor introducí el correo del contacto:')
    
    # Se añade un nuevo contacto al diccionario 'agenda'
    # La clave será el nombre del contacto, y el valor será otro diccionario con teléfono y correo
    agenda[nombre] = {'Telefono': telefono, 'Correo': email}
    
    print(f'Se ha agregado el contacto {nombre} exitosamente!')

def eliminar_contacto(agenda):
    # Solicita el nombre del contacto a eliminar
    nombre = input('Ingrese el nombre del contacto que desea eliminar:')
    
    # Verifica si el nombre existe en la agenda
    if nombre in agenda:
        # Si el contacto existe, lo elimina del diccionario
        del agenda[nombre]
        print(f'El contacto de {nombre} ha sido eliminado correctamente.')
    else:
        # Si no existe, muestra un mensaje de error
        print(f'No se ha encontrado un contacto con el nombre {nombre}.')

def buscar_contacto(agenda):
    # Solicita el nombre del contacto que se desea buscar
    nombre = input('Por favor ingrese el nombre del contacto que busca:')
    
    # Verifica si el nombre del contacto está en el diccionario 'agenda'
    if nombre in agenda:
        # Si el contacto existe, imprime los datos asociados
        # Se accede a los valores del diccionario con: agenda[nombre]["Telefono"] y agenda[nombre]["Correo"]
        print(f'Nombre: {nombre}')
        print(f'Telefono: {agenda[nombre]["Telefono"]}')  # Accediendo al teléfono del contacto
        print(f'Correo: {agenda[nombre]["Correo"]}')  # Accediendo al correo del contacto
    else:
        # Si el contacto no existe, muestra un mensaje de error
        print(f'El contacto {nombre} no ha sido encontrado en la agenda.')

def listar_contacto(agenda):
    # Verifica si la agenda tiene contactos
    if agenda:
        print('\nLista de Contactos:')
        
        # Recorre el diccionario 'agenda' para mostrar todos los contactos
        for nombre, info in agenda.items():
            # 'nombre' es la clave (el nombre del contacto)
            # 'info' es el valor, que es un diccionario con los datos 'Telefono' y 'Correo'
            print(f'Nombre: {nombre}')
            print(f'Telefono: {info["Telefono"]}')  # Accediendo al teléfono del contacto
            print(f'Email: {info["Correo"]}')  # Accediendo al correo del contacto
            print('-' * 20)  # Separador visual entre contactos
    else:
        # Si la agenda está vacía, lo indica al usuario
        print("La agenda aún está vacía.")

def gestionar_agenda():
    # Crea un diccionario vacío para almacenar los contactos
    agenda = {}

    # Bucle principal para gestionar las operaciones del usuario
    while True:
        # Muestra el menú de opciones
        mostrar_menu()

        opcion = input('Por favor elija una opción:')
        # Lógica de las opciones del menú
        if opcion == '1':
            agregar_contacto(agenda)
        elif opcion == '2':
            eliminar_contacto(agenda)
        elif opcion == '3':
            buscar_contacto(agenda)
        elif opcion == '4':
            listar_contacto(agenda)
        elif opcion == '5':
            # Opción para salir del programa
            print('Saliendo de la agenda.')
            break  # Sale del bucle para finalizar el programa
        else:
            # Si elige una opción no válida, se le indica al usuario
            print('Por favor, selecciona una opción válida.')

gestionar_agenda()
