 ###################################
 # 01. Definir una funcion max() que tomo como argumento dos números enteros y devuelva el mayor de ellos

def valorMax(n1 , n2):
    return n1 if n1 > n2 else n2

#print(valorMax(5, 10))

######################################

# 02. Escribe una función que verifique si una cadena de paréntesis (de diferentes tipos: {}, [], ()) está correctamente balanceada.

def esta_balanceada(cadena):
    pares = {')': '(', ']': '[', '}': '{'}
    pila = []

    for caracter in cadena:
        if caracter in pares.values():
            pila.append(caracter) 
        elif caracter in pares.keys(): 
            if not pila or pila[-1] != pares[caracter]:
                return False
            pila.pop()  

    return len(pila) == 0


# Asserts para probar la función
assert esta_balanceada("()") == True
assert esta_balanceada("()[]{}") == True
assert esta_balanceada("(]") == False
assert esta_balanceada("([)]") == False
assert esta_balanceada("{[]}") == True
assert esta_balanceada("") == True
assert esta_balanceada("(((((())))))") == True
assert esta_balanceada("(((()") == False

print("¡Todos los tests pasan correctamente!")




