#funcion pura es la que no tiene efectos secundarios, no se debe 

#Ejemplo1 inmutabilidad
variable_global=10 #variable global

def aumentar_variable ():
    return variable_global + 1 

print(aumentar_variable())



#segundo ejemplo
def contar_palabras(texto):
    return len(texto.split())

oracion = "El tema de hoy es inmutabilidad en Python"
print(contar_palabras(oracion))

contardor_globalm = 0 


#ejemplo tres
contador_global = 0 

def contador_palabras_no_funcional(texto)
    global contador_global
    contador_global = len(texto.split())