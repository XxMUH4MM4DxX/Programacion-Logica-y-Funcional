def menu():
    print("\n---- Menú de Operaciones ----")
    print("1. Multiplicar")
    print("2. Dividir")
    print("3. Salir")
    return int(input("Elija una opción: "))

def main():
    multiplicar = lambda a, b: a * b
    dividir = lambda a, b: a / b if b != 0 else "No se puede dividir por cero."

    while True:
        opcion = menu()

        if opcion == 1:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"La multiplicación de {a} y {b} es: {multiplicar(a, b)}")

        elif opcion == 2:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"La división de {a} entre {b} es: {dividir(a, b)}")

        elif opcion == 3:
            print("¡Gracias por usar el sistema!")
            break

        else:
            print("Opción no válida. Por favor elija una opción correcta.")

main()