def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: División por cero"

def menu():
    print("---- Menu de la Calculadora ----")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Salir")

    return int(input("Ingrese una opción: "))

def main():
    while True:
        opcion = menu()
        
        if opcion == 5:
            print("¡HASTA LA VISTA BABE!")
            break
        
        if opcion in [1, 2, 3, 4]:
            x = float(input("Ingrese el primer número (x): "))
            y = float(input("Ingrese el segundo número (y): "))
            
            if opcion == 1:
                print(f"El resultado de la suma es: {suma(x, y)}")
            elif opcion == 2:
                print(f"El resultado de la resta es: {resta(x, y)}")
            elif opcion == 3:
                print(f"El resultado de la multiplicación es: {multiplicacion(x, y)}")
            elif opcion == 4:
                print(f"El resultado de la división es: {division(x, y)}")
        else:
            print("Opción no válida!")

main()
