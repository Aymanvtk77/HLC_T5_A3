def duplicados(lista_palabras):
 return list(set(lista_palabras))
entrada = ["hola", "mundo", "hola", "jacobo", "mundo"]
salida = duplicados(entrada)
print(salida)