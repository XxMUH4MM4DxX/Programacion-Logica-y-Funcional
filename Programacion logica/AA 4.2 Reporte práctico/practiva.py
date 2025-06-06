# Variables globales
humedad_suelo = "baja"
temperatura = 35
hora = 20
pronostico_lluvia = False

def hora_adecuada():
    global hora
    return hora and hora < 10 or hora > 18

def activar_riego():
    global humedad_suelo, pronostico_lluvia
    return humedad_suelo == "baja" and (pronostico_lluvia==False) and hora_adecuada()

def alerta_calor():
    global temperatura
    return temperatura and temperatura >= 32

def estado_riego():
    if activar_riego():
        return "Activado"
    else:
        return "No activado"

def recomendacion():
    if activar_riego() and alerta_calor():
        print("Alerta: Riego activado con temperatura alta. Considere riego nocturno o por goteo.")
    else:
        print("Sin recomendaciones especiales para el riego.")
