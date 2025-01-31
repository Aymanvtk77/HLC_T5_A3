def diccionario():
    diccionario = {}
    for numero in range(1, 6):
        diccionario[numero] = numero ** 2
    return diccionario
resultado = diccionario()
print(resultado)