def mostrar_inventario(inventario):
    if inventario:
        for i, (nombre, cantidad) in enumerate(inventario.items(), 1):
            print(f"{i}. {nombre} - {cantidad} unidades")
    else:
        print("El inventario está vacío.")

def mostrar_mensaje(mensaje):
    print(mensaje)

def agregar_equipo(inventario, nombre, cantidad, callback):
    inventario[nombre] = inventario.get(nombre, 0) + cantidad
    callback(f"✅ Se agregaron {cantidad} unidades de '{nombre}' al inventario.")

def retirar_equipo(inventario, nombre, cantidad, callback):
    if nombre in inventario and inventario[nombre] >= cantidad:
        inventario[nombre] -= cantidad
        callback(f"⚡ {cantidad} unidades de '{nombre}' fueron retiradas.")
        if inventario[nombre] == 0:
            del inventario[nombre]
    else:
        callback("❌ No hay suficiente cantidad o el equipo no existe en el inventario.")

def buscar_equipo(inventario, nombre, callback):
    if nombre in inventario:
        callback(f"🔍 '{nombre}' está disponible con {inventario[nombre]} unidades.")
    else:
        callback(f"❌ '{nombre}' no se encuentra en el inventario.")

def menu():
    print("\n---- 🖥️ Inventario de Laboratorio de Sistemas ----")
    print("1.- Mostrar inventario")
    print("2.- Agregar equipo")
    print("3.- Retirar equipo")
    print("4.- Buscar equipo")
    print("5.- Salir")
    return int(input("Ingrese una opción: "))

def main():
    inventario = {}

    while True:
        opcion = menu()

        if opcion == 1:
            mostrar_inventario(inventario)

        elif opcion == 2:
            nombre = input("Ingrese el nombre del equipo: ")
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            agregar_equipo(inventario, nombre, cantidad, mostrar_mensaje)

        elif opcion == 3:
            nombre = input("Ingrese el nombre del equipo: ")
            cantidad = int(input("Ingrese la cantidad a retirar: "))
            retirar_equipo(inventario, nombre, cantidad, mostrar_mensaje)

        elif opcion == 4:
            nombre = input("Ingrese el nombre del equipo a buscar: ")
            buscar_equipo(inventario, nombre, mostrar_mensaje)

        elif opcion == 5:
            print("👋 ¡Hasta luego! Gracias por utilizar el sistema.")
            break

        else:
            print("⚠️ Opción no válida. Inténtelo de nuevo.")

main()
