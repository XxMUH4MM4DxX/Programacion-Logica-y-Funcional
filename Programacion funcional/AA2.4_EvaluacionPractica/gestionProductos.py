def procesar_lista_productos(productos):
   
    productos_ordenados = sorted(productos, key=lambda x: x.lower())
   
    cadena_ordenada = ', '.join(productos_ordenados)

    slugs = list(map(lambda x: x.lower().replace(' ', '-'), productos_ordenados))
    
    return slugs, cadena_ordenada

productos = ["frijoles refritos", "Coca Cola", "Zumo de Naranja", "Café de Olla", "Gorditas de Chicharron", "Huevos Revueltos"]

slugs, cadena_ordenada = procesar_lista_productos(productos)

print("Lista de slugs:", slugs)
print("Cadena de nombres ordenados alfabéticamente:", cadena_ordenada)
