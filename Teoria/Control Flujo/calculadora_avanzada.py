
print("Bienvenidos a la calculadora")  
print("Para salir escribe 'salir'")    
print("Las operaciones son: suma, resta, multi, div")  

# Inicializa la variable resultado como None
resultado = None  

# Comienza un bucle infinito para que la calculadora funcione hasta que el usuario decida salir
while True:  
    # Si resultado es None, se espera que el usuario ingrese un número
    if resultado is None:  
        entrada = input("Ingrese número:") 
        if entrada.lower() == "salir":  
            break
        # Verifica si la entrada es un número entero (positivo o negativo)
        if entrada.isdigit() or (entrada.startswith('-') and entrada[1:].isdigit()):  
            resultado = int(entrada)  # Convierte la entrada a un entero y lo asigna a resultado
        else:
            print("Por favor,.ingrese un número válido.")  
            continue  # Vuelve al inicio del bucle

    # Solicita al usuario que ingrese una operación
    op = input("Ingresa operación:")  
    if op.lower() == "salir":  
        break

    n2 = input("Ingresa siguiente número:")  
    if n2.lower() == "salir":  
        break

    # Verifica si el segundo número es válido
    if n2.isdigit() or (n2.startswith('-') and n2[1:].isdigit()):  
        n2 = int(n2)  # Convierte la entrada a un entero
    else:
        print("Por favor, ingrese un número válido.")  
        continue 

    # Realiza la operación solicitada
    if op.lower() == "suma":  
        resultado += n2  
    elif op.lower() == "resta":  
        resultado -= n2  
    elif op.lower() == "multi":  
        resultado *= n2 
    elif op.lower() == "div":  
        if n2 == 0:  # 
            print("No se puede dividir entre cero.")  
            continue  
        resultado /= n2  # Divide el resultado por el segundo número
    else:
        print("Operación no válida.")  
        continue  

   
    print(f"El resultado es: {resultado}")  
