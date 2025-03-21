def mostrar_tareas(tareas):
    for i, tarea in enumerate(tareas, 1):
        estado = "Completada" if tarea['completada'] else "Pendiente"
        print(f"{i}. {tarea['nombre']} - {estado}")

def filtrar_tareas(tareas, filtro_func):
    return list(filter(filtro_func, tareas))

def agregar_tarea(tareas, nombre):
    tareas.append({'nombre': nombre, 'completada': False})

def marcar_como_completada(tareas, index):
    if 0 <= index < len(tareas):
        tareas[index]['completada'] = True

def filtrar_completadas(tarea):
    return tarea['completada']

def filtrar_pendientes(tarea):
    return not tarea['completada']

def aplicar_accion_a_tarea(tareas, accion_func, *args):
    return accion_func(tareas, *args)

def menu():
    print("\n---- Administrador de Tareas Escolares ----")
    print("1.- Mostrar todas las tareas")
    print("2.- Agregar una nueva tarea")
    print("3.- Marcar tarea como completada")
    print("4.- Filtrar tareas completadas")
    print("5.- Filtrar tareas pendientes")
    print("6.- Salir")
    return int(input("Ingrese una opción: "))

def main():
    tareas = []

    while True:
        opcion = menu()

        if opcion == 1:
            mostrar_tareas(tareas)
        elif opcion == 2:
            nombre_tarea = input("Ingrese el nombre de la tarea: ")
            aplicar_accion_a_tarea(tareas, agregar_tarea, nombre_tarea)
        elif opcion == 3:
            mostrar_tareas(tareas)
            tarea_num = int(input("Ingrese el número de la tarea a marcar como completada: ")) - 1
            aplicar_accion_a_tarea(tareas, marcar_como_completada, tarea_num)
        elif opcion == 4:
            completadas = filtrar_tareas(tareas, filtrar_completadas)
            print("Tareas completadas:")
            mostrar_tareas(completadas)
        elif opcion == 5:
            pendientes = filtrar_tareas(tareas, filtrar_pendientes)
            print("Tareas pendientes:")
            mostrar_tareas(pendientes)
        elif opcion == 6:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

main()
