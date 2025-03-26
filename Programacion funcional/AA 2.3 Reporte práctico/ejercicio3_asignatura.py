asignaturas_vii = ["Programacion web"]
print(asignaturas_vii)

#crea una lista que contiene la lista de asignaturas_vii y una nueva asignatura

nueva_lista = asignaturas_vii + ["Bases de datos"]
print(nueva_lista)

# crea una funcion agregar_asignatura  que reciba dos parametros, una lista y una asignatura, la funcion debe devolver la lista y la asignatura
def agregar_asignatura(lista, asignatura):
    return lista + asignatura 

print(agregar_asignatura(asignaturas_vii, [input("Ingrese una nueva materia: " )]))
