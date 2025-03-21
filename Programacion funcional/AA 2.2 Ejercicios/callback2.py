productos = {
    1: {"nombre": "Sandwich", "precio": 25},
    2: {"nombre": "Jugo", "precio": 15},
    3: {"nombre": "Papas", "precio": 10},
    4: {"nombre": "Agua", "precio": 12},
    5: {"nombre": "Galletas", "precio": 8},
}

def mostrar_menu():
    print("\n--- 🥪 Tienda de Comida Escolar 🥤 ---")
    for key, producto in productos.items():
        print(f"{key}. {producto['nombre']} - ${producto['precio']}")
    print("6. Finalizar compra")

def agregar_producto(carrito, producto_num, callback):
    if producto_num in productos:
        carrito.append(productos[producto_num])
        print(f"✅ {productos[producto_num]['nombre']} agregado al carrito.")
        callback(carrito) 
    else:
        print("❗ Opción inválida. Elige un número válido.")

def mostrar_carrito(carrito):
    print("\n🛒 Productos en tu carrito:")
    if not carrito:
        print("Tu carrito está vacío.")
    else:
        for i, producto in enumerate(carrito, 1):
            print(f"{i}. {producto['nombre']} - ${producto['precio']}")
        print(f"Total actual: ${sum(p['precio'] for p in carrito)}")

def calcular_total(carrito):
    return sum(producto['precio'] for producto in carrito)

def procesar_compra(carrito, callback):
    if not carrito:
        print("❗ No has seleccionado ningún producto.")
    else:
        total = calcular_total(carrito)
        callback(carrito, total) 

def mostrar_resumen(carrito, total):
    print("\n🧾 Resumen de tu compra:")
    for producto in carrito:
        print(f"- {producto['nombre']} - ${producto['precio']}")
    print(f"💰 Total a pagar: ${total}")
    print("✅ ¡Gracias por tu compra en la Tienda Escolar!")

def main():
    carrito = []
    
    while True:
        mostrar_menu()
        opcion = int(input("👉 Elige una opción: "))

        if opcion == 6:
            procesar_compra(carrito, mostrar_resumen)  
            break
        else:
            agregar_producto(carrito, opcion, mostrar_carrito)

main()
