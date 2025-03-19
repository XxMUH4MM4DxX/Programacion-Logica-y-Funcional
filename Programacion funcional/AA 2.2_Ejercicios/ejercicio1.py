def preparar_cafe():
    return "cafe"

print (preparar_cafe())


def ordenar_cafe(num_tazas):
    tazas_cafe=[preparar_cafe() for _ in range(num_tazas)]
    return tazas_cafe

cafe_para_grupoB = ordenar_cafe(10) #llamamos a la funcion con numero de tazas
print(cafe_para_grupoB)

#print(preparar_cafe()) 
# vamos a ordenar hotcakes vamos a tener una f que no va a recibir parametros y va a retornar un emogi de 
# 2 que va a recibir un argumento nume de piezas almacena lista hotscakes
