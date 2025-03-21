def consultar_saldo(saldo):
    return f"Saldo disponible: ${saldo}"

def ingresar_dinero(saldo):
    cantidad = float(input("Ingrese la cantidad a depositar: "))
    saldo += cantidad
    return saldo, f"Has depositado ${cantidad}. Saldo actual: ${saldo}"

def retirar_dinero(saldo):
    cantidad = float(input("Ingrese la cantidad a retirar: "))
    if cantidad <= saldo:
        saldo -= cantidad
        return saldo, f"Has retirado ${cantidad}. Saldo actual: ${saldo}"
    else:
        return saldo, "Fondos insuficientes."

def mostrar_menu():
    print("\n------------------ BANCO DEL BIENESTAR ------------------")
    print("1.- Consultar saldo")
    print("2.- Ingresar dinero")
    print("3.- Retirar dinero")
    print("4.- Salir")
    return int(input("Seleccione una opción: "))

def elegir_operacion(opcion):
    operaciones = {
        1: consultar_saldo,
        2: ingresar_dinero,
        3: retirar_dinero
    }
    return operaciones.get(opcion, None)

def ejecutar_operacion(operacion, saldo):
    if operacion == consultar_saldo:
        return operacion(saldo)
    else:
        saldo, mensaje = operacion(saldo)
        return saldo, mensaje

def main():
    saldo = 1000
    while True:
        opcion = mostrar_menu()
        if opcion == 4:
            print("¡Gracias por usar el BANCO DEL BIENESTAR!")
            break

        operacion = elegir_operacion(opcion)  # Asignar la función correspondiente a una variable
        if operacion:  # Verifica si la operación es válida
            if operacion == consultar_saldo:
                mensaje = ejecutar_operacion(operacion, saldo)  # Pasar la función como argumento
                print(mensaje)
            else:
                saldo, mensaje = ejecutar_operacion(operacion, saldo)  # Ingreso o retiro de dinero
                print(mensaje)
        else:
            print("Opción no válida!")

main()
