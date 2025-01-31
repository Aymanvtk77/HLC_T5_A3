def calcular_suma_promedio(numeros):
    suma = sum(numeros)
    promedio = suma / len(numeros)
    return suma, promedio
numeros = [10, 20, 30]
suma, promedio = calcular_suma_promedio(numeros)
print(f"suma: {suma}, promedio: {promedio}")