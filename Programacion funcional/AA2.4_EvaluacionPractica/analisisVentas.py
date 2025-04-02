from functools import reduce

listaventaPesos = [
    {"cantidad": 1500},
    {"cantidad": 2500},
    {"cantidad": 3200},
    {"cantidad": 4500},
    {"cantidad": 6000},
    {"cantidad": 1200},
    {"cantidad": 8000},
]

tipo_cambio = 20.37  

total_ventas_pesos = reduce(lambda acumulador, venta: acumulador + venta["cantidad"], listaventaPesos, 0)
promedio_ventas_pesos = total_ventas_pesos / len(listaventaPesos)
print(f"Promedio de ventas por día en pesos mexicanos: {promedio_ventas_pesos:.2f} MXN")

ventas_dolares = list(map(lambda venta: {**venta, "cantidad_dolares": venta["cantidad"] / tipo_cambio}, listaventaPesos))
print("Ventas en dólares:", ventas_dolares)


ventas_filtradas = list(filter(lambda venta: venta["cantidad_dolares"] > 150, ventas_dolares))
print("Ventas mayores a 150 dólares:", ventas_filtradas)


suma_total_ventas_filtradas = reduce(lambda acumulador, venta: acumulador + venta["cantidad_dolares"], ventas_filtradas, 0)
print(f"Suma total de ventas mayores a 150 dólares: {suma_total_ventas_filtradas:.2f} USD")
