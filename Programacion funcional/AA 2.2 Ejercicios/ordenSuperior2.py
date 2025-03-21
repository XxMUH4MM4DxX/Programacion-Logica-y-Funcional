def ingresar_calificaciones():
    cantidad = int(input("¿Cuántas calificaciones vas a ingresar? "))
    calificaciones = []
    for i in range(cantidad):
        calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
        calificaciones.append(calificacion)
    return calificaciones

def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

def evaluar_promedio(promedio):
    if promedio >= 9:
        return "¡Felicidades campeón! Has sacado un excelente promedio."
    elif promedio >= 8:
        return "Vas bien, ¡échale ganas!"
    elif promedio >= 7:
        return "Puedes mejorar, sigue esforzándote."
    else:
        return "Reprobaste, debes estudiar más."

def mostrar_resultado(func_calcular, func_evaluar):
    calificaciones = ingresar_calificaciones()
    promedio = func_calcular(calificaciones)
    mensaje = func_evaluar(promedio)
    print(f"Tu promedio es: {promedio:.2f}")
    print(mensaje)

def evaluar_calificaciones():
    return mostrar_resultado(calcular_promedio, evaluar_promedio)

evaluar_calificaciones()
