n1 = input("Ingresa un primer número:")
n2 = input("Ingresa un segundo número:")


n1 = int(n1)
n2 = int(n2)


suma = n1 + n2
resta = n1 - n2
div = n1 * n2
multi = n1 / n2

mensaje = f"""

Para los números {n1} y {n2} , el resultado de la suma es: {suma}
Para los números {n1} y {n2} , el resultado de la resta es: {resta}
Para los números {n1} y {n2} , el resultado de la multiplicación es: {multi}
Para los números {n1} y {n2} , el resultado de la división es: {div}

"""

print(mensaje)