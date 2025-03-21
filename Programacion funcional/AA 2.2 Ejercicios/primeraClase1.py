def mostrar_productos():
    productos = {
        1: {"nombre": "Camiseta Burberry", "precio": 250, "disponibilidad": True, "marca": "Burberry"},
        2: {"nombre": "Pantalón Dolce & Gabbana", "precio": 500, "disponibilidad": True, "marca": "Dolce & Gabbana"},
        3: {"nombre": "Chaqueta Calvin Klein", "precio": 700, "disponibilidad": True, "marca": "Calvin Klein"},
        4: {"nombre": "Zapatos Salvatore Ferragamo", "precio": 850, "disponibilidad": True, "marca": "Salvatore Ferragamo"},
    }
    return productos

def realizar_compra(saldo, producto_num, productos_disponibles):
    if producto_num in productos_disponibles:
        producto = productos_disponibles[producto_num]
        if producto["disponibilidad"]:
            if saldo >= producto["precio"]:
                saldo -= producto["precio"]
                producto["disponibilidad"] = False
                return f"Has comprado {producto['nombre']} de {producto['marca']} por ${producto['precio']}. Saldo restante: ${saldo}"
            else:
                return "Saldo insuficiente para realizar la compra."
        else:
            return f"{producto['nombre']} de {producto['marca']} está agotada."
    else:
        return "Producto no disponible."

def consultar_saldo(saldo):
    return f"Tu saldo disponible es: ${saldo}"

def ingresar_saldo(saldo):
    cantidad = float(input("Ingrese la cantidad a depositar: "))
    saldo += cantidad
    return f"Has ingresado ${cantidad}. Nuevo saldo: ${saldo}"

def menu():
    print("\n---- Tienda de Ropa de Diseñador ----")
    print("1.- Ver productos disponibles")
    print("2.- Realizar una compra")
    print("3.- Consultar saldo")
    print("4.- Ingresar saldo")
    print("5.- Salir")
    return int(input("Ingrese una opción: "))

def obtener_funcion(opcion):
    if opcion == 1:
        return mostrar_productos
    elif opcion == 2:
        return realizar_compra
    elif opcion == 3:
        return consultar_saldo
    elif opcion == 4:
        return ingresar_saldo
    else:
        return None

def ejecutar_funcion(funcion, *args):
    return funcion(*args)

def main():
    saldo = 1000
    productos_disponibles = mostrar_productos()
    
    while True:
        opcion = menu()
        funcion = obtener_funcion(opcion)
        
        if funcion:
            if opcion == 1:
                print("Productos disponibles:")
                for key, producto in productos_disponibles.items():
                    disponibilidad = "Disponible" if producto["disponibilidad"] else "Agotada"
                    print(f"{key}. {producto['nombre']} ({producto['marca']}) - ${producto['precio']} ({disponibilidad})")
            elif opcion == 2:
                producto_num = int(input("Ingrese el número del producto que desea comprar: "))
                print(ejecutar_funcion(funcion, saldo, producto_num, productos_disponibles))
            elif opcion == 3:
                print(ejecutar_funcion(funcion, saldo))
            elif opcion == 4:
                print(ejecutar_funcion(funcion, saldo))
            elif opcion == 5:
                print("¡Gracias por visitar nuestra tienda de diseñador!")
                break
        else:
            print("Opción no válida, por favor elija otra opción.")

main()
