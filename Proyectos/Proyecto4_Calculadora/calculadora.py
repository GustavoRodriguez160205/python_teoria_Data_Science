def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Error: No es posible dividir entre 0.')
        return None

def multiplicacion(a, b):
    return a * b 

def consola():
    while True:
        print('\nBienvenido a mi calculadora')
        print('Selecciona la operación que deseas realizar:')
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicación')
        print('4. División')
        print('5. Salir')

        opcion = input('Ingresa el número de la operación: ')

      
        if opcion == '5':
            print('Saliendo de la calculadora.')
            break

       
        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = int(input('Ingresa el primer número: '))
                num2 = int(input('Ingresa el segundo número: '))
            except ValueError:
                print("Error: Por favor ingresa números válidos.")
                continue

          
            resultado = None
            if opcion == '1':
                resultado = suma(num1, num2)
            elif opcion == '2':
                resultado = resta(num1, num2)
            elif opcion == '3':
                resultado = multiplicacion(num1, num2)
            elif opcion == '4':
                resultado = division(num1, num2)

            # Imprimir el resultado si no hubo error
            if resultado is not None:
                print('Resultado:', resultado)
        else:
            print('Opción no válida. Intenta nuevamente.')


consola()
