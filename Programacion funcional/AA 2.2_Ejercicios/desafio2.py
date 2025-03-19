def preparar_pizza():
    return "🍕"

def preparar_hamburgesa():
    return "🍔"

def preparar_hotdog():
    return "🌭"

def calcular_bonus(numero_porciones):
    if numero_porciones > 2:
        return "Coca Gratis"
    else:
        return ""  # Retornamos una cadena vacía si no hay bonus

def ordenar_alimento(funcion, numero_porciones):
    lista_porciones = [funcion() for _ in range(numero_porciones)]
    bonus = calcular_bonus(numero_porciones)  # Llamamos a la función calcular_bonus
    return lista_porciones, bonus  # Devolvemos tanto las porciones como el bonus

# Ejemplo de uso:
ordenar_alimento_grupoA = ordenar_alimento(preparar_pizza, 2)
ordenar_alimento_grupoB = ordenar_alimento(preparar_hamburgesa, 3)
ordenar_alimento_grupoC = ordenar_alimento(preparar_hotdog, 2)

# Imprimimos los resultados
print(ordenar_alimento_grupoA)  # Debería mostrar las porciones y el bonus
print(ordenar_alimento_grupoB)  # Debería mostrar las porciones y el bonus
print(ordenar_alimento_grupoC)  # Debería mostrar las porciones y el bonus
