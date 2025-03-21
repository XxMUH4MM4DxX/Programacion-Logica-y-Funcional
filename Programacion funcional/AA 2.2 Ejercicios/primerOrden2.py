def menu():
    print("---- Menu de opciones ----")
    print("1 - Convertir Decimal a Binario")
    print("2 - Convertir Binario a Decimal")
    return int(input("Ingrese una opción: "))

def decimal_a_binario(decimal):
    return bin(decimal)[2:]  

def binario_a_decimal(binario):
    return int(binario, 2)  

def main():
    opcion = menu()  
    resultado = ''
    
    if opcion == 1:
        print("-- Convertir Decimal a Binario --")
        decimal = int(input("Ingrese un número decimal: "))
        resultado = decimal_a_binario(decimal)
    elif opcion == 2:
        print("-- Convertir Binario a Decimal --")
        binario = input("Ingrese un número binario: ")
        resultado = binario_a_decimal(binario)
    else:
        print("❌Error Opción Inválida❌")  

    if (opcion < 3 and opcion > 0):
        print(f"El resultado es: {resultado}")  

main()
