def preparar_cafe_a():
    return "cafe_americano"

def preparar_cafe_o():
    return "cafe_olla"

def ordenar_cafe(funcion, numero_tazas):
    tazas_cafe = [funcion() for _ in range(numero_tazas)]
    return tazas_cafe

ordenar_cafe_grupoA = ordenar_cafe(preparar_cafe_a, 7)
ordenar_cafe_grupoB = ordenar_cafe(preparar_cafe_o, 7)

print(ordenar_cafe_grupoA, ordenar_cafe_grupoB)

#