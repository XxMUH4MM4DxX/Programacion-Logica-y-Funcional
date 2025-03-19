def preparar_hotcakes():
    return "🥞"

print (preparar_hotcakes())

def ordenar_hotcake(num_piezas):
    piezas_hotcakes=[preparar_hotcakes() for _ in range(num_piezas)]
    return piezas_hotcakes

hotcake_familia = ordenar_hotcake( int (input ('Cuantos son en tu familia? : ')))
print(hotcake_familia)

# cafe_para_grupoB = ordenar_cafe(10) #llamamos a la funcion con numero de tazas
# print(cafe_para_grupoB)