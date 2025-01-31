def obtener_divisor(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores
entrada = 12
print(obtener_divisor(entrada))