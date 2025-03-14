# Sombrero seleccionador de ramas de sistemas computacionales 🧙‍♂️

# Inicialización de puntajes para cada rama.
redes = 0
bases_de_datos = 0
desarrollo_software = 0
programacion_hardware = 0
modelado_3d = 0
gestion_proyectos = 0

# Título del programa.
print('===============')
print('El sombrero seleccionador de ramas de sistemas computacionales 🧙‍♂️')
print('===============')

# Pregunta 1
print('P1) ¿Te gustaría trabajar con redes de computadoras y la conexión de dispositivos?')
print('  1) Sí, me interesa la comunicación entre dispositivos')
print('  2) No mucho, prefiero desarrollar hardware')
print('  3) Definitivamente no')
respuesta = int(input('Ingresa respuesta (1-3): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    programacion_hardware += 1
elif respuesta == 3:
    print("Respuesta rechazada para Redes.")
else:
    print('Respuesta incorrecta.')

# Pregunta 2
print('\nP2) ¿Te atrae la idea de diseñar y gestionar bases de datos?')
print('  1) Sí, me interesa organizar y almacenar grandes cantidades de información')
print('  2) No mucho, prefiero desarrollar aplicaciones')
print('  3) Definitivamente no')
respuesta = int(input('Ingresa tu respuesta (1-3): '))

if respuesta == 1:
    bases_de_datos += 2
elif respuesta == 2:
    desarrollo_software += 2
elif respuesta == 3:
    print("Respuesta rechazada para Bases de Datos.")
else:
    print('Respuesta incorrecta.')

# Pregunta 3
print('\nP3) ¿Te apasiona desarrollar software y aplicaciones?')
print('  1) Sí, me encanta programar y crear aplicaciones')
print('  2) No tanto, prefiero trabajar con hardware')
print('  3) Definitivamente no')
respuesta = int(input('Ingresa tu respuesta (1-3): '))

if respuesta == 1:
    desarrollo_software += 4
elif respuesta == 2:
    programacion_hardware += 4
elif respuesta == 3:
    print("Respuesta rechazada para Desarrollo de Software.")
else:
    print('Respuesta incorrecta.')

# Pregunta 4
print('\nP4) ¿Te gustaría trabajar en la creación y diseño de modelos 3D?')
print('  1) Sí, me fascina el diseño gráfico y los modelos 3D')
print('  2) No mucho, prefiero la gestión de proyectos')
print('  3) Definitivamente no')
respuesta = int(input('Ingresa tu respuesta (1-3): '))

if respuesta == 1:
    modelado_3d += 3
elif respuesta == 2:
    gestion_proyectos += 3
elif respuesta == 3:
    print("Respuesta rechazada para Modelado 3D.")
else:
    print('Respuesta incorrecta.')

# Pregunta 5
print('\nP5) ¿Te gustaría ser responsable de la gestión de proyectos de software?')
print('  1) Sí, me interesa liderar equipos y gestionar proyectos')
print('  2) No, prefiero concentrarme en el desarrollo técnico')
print('  3) Definitivamente no')
respuesta = int(input('Ingresa tu respuesta (1-3): '))

if respuesta == 1:
    gestion_proyectos += 3
elif respuesta == 2:
    desarrollo_software += 3
elif respuesta == 3:
    print("Respuesta rechazada para Gestión de Proyectos.")
else:
    print('Respuesta incorrecta.')

# Pregunta 6 - Desarrollo de Hardware
print('\nP6) ¿Te gustaría desarrollar hardware, como circuitos y dispositivos electrónicos?')
print('  1) Sí, me encanta trabajar con hardware y dispositivos electrónicos')
print('  2) No mucho, prefiero las redes')
print('  3) Definitivamente no')
respuesta = int(input('Ingresa tu respuesta (1-3): '))

if respuesta == 1:
    programacion_hardware += 5
elif respuesta == 2:
    redes += 5
elif respuesta == 3:
    print("Respuesta rechazada para Desarrollo de Hardware.")
else:
    print('Respuesta incorrecta.')

# Resultados finales
print("\nResultados finales:")
print(f"Redes: {redes} puntos")
print(f"Bases de Datos: {bases_de_datos} puntos")
print(f"Desarrollo de Software: {desarrollo_software} puntos")
print(f"Programación Hardware: {programacion_hardware} puntos")
print(f"Modelado 3D: {modelado_3d} puntos")
print(f"Gestión de Proyectos: {gestion_proyectos} puntos")

# Determinación de la rama con mayor puntaje
max_puntaje = max(redes, bases_de_datos, desarrollo_software, programacion_hardware, modelado_3d, gestion_proyectos)

if max_puntaje == redes:
    print('¡Tu rama recomendada es: Redes!')
elif max_puntaje == bases_de_datos:
    print('¡Tu rama recomendada es: Bases de Datos!')
elif max_puntaje == desarrollo_software:
    print('¡Tu rama recomendada es: Desarrollo de Software!')
elif max_puntaje == programacion_hardware:
    print('¡Tu rama recomendada es: Programación Hardware!')
elif max_puntaje == modelado_3d:
    print('¡Tu rama recomendada es: Modelado 3D!')
else:
    print('¡Tu rama recomendada es: Gestión de Proyectos de Software!')
