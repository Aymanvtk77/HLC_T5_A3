def diccionario_longitudes(lista_palabras):
    diccionario = {}
    for palabra in lista_palabras:
        diccionario[palabra] = len(palabra)
    return diccionario
palabras = ["Beti", "sevilla", "madrid"]
resultado = diccionario_longitudes(palabras)
print(resultado)