#Apartir del codigo base modifica la funcion cuadradosLista utilizando cualquier convinacion de map(), filter(), reduce().
#La funcion deberia devolver un nuevo arreglo que contenga que contenga los cuadrados unicamente de los enteros posistivo (Los numeros decimales no son enteros ) cuando se le pase un arreglo de numeros reales.
#un ejemplo de un arreglo de numeros reales es [-3, 4.8, 5, 3, -3.2]

#Nota: LA FUNCION NO DEBE DE USAR NINGUN TIPO DE BLUCLES FOR O WHILE NI LA FUNCION forEach

#Escribe el codigo aqui
def cuadradrosLista(arreglo):
    return list(map(lambda n: n**2, filter(lambda n: isinstance(n, int) and n > 0, arreglo)))


# Ejemplo de uso
cuadrados_enteros = cuadradrosLista([-3, 4.8, 5, 3, -3.2])
print(cuadrados_enteros)
