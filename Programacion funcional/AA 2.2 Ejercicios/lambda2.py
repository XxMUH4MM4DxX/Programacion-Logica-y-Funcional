def menu():
    print("\n---- Menú de Operaciones ----")
    print("1.- Sumar dos números")
    print("2.- Restar dos números")
    print("3.- Salir")
    return int(input("Ingrese una opción: "))

def main():
    while True:
        opcion = menu()

        if opcion == 1:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            suma = (lambda a, b: a + b)  
            resultado = suma(num1, num2)
            print(f"La suma es: {resultado}")
        elif opcion == 2:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resta = (lambda a, b: a - b)  
            resultado = resta(num1, num2)
            print(f"La resta es: {resultado}")
        elif opcion == 3:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

main()
