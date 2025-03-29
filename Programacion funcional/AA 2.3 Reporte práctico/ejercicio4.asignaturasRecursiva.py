
def agregar_asignatura(lista):
    asig_nueva = input ("ESCRIBE LA ASIGNATURA NUEVA: ")
    if asig_nueva =="exit":
        return lista
    return agregar_asignatura(lista + [asig_nueva])# recursion

asignatura_vii = ["Inteligencia Artificial, Redes, Front-end, "]
nueva_lista= agregar_asignatura(asignatura_vii)
print(asignatura_vii)
print(nueva_lista)


