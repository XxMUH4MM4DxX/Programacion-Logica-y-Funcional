import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from functools import reduce

respuestas_acumuladas = []

def calcular_promedio(lista):
    return round(sum(lista) / len(lista), 2) if lista else 0

def validar_respuestas_recursivas(lista):
    if not lista:
        return True
    return 1 <= lista[0] <= 10 and validar_respuestas_recursivas(lista[1:])

def sumar_respuestas_recursivas(lista):
    if not lista:
        return 0
    return lista[0] + sumar_respuestas_recursivas(lista[1:])

def contar_elementos_recursivos(lista):
    if not lista:
        return 0
    return 1 + contar_elementos_recursivos(lista[1:])

def map_recursivo(func, lista):
    if not lista:
        return []
    return [func(lista[0])] + map_recursivo(func, lista[1:])

def filter_recursivo(func, lista):
    if not lista:
        return []
    if func(lista[0]):
        return [lista[0]] + filter_recursivo(func, lista[1:])
    return filter_recursivo(func, lista[1:])

def reduce_recursivo(func, lista, valor_inicial=None):
    if not lista:
        return valor_inicial
    if valor_inicial is None:
        return reduce_recursivo(func, lista[1:], lista[0])
    return reduce_recursivo(func, lista[1:], func(valor_inicial, lista[0]))

class EncuestaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Encuesta de Evaluación TecNM FCP")
        self.aspectos = ["Actividades", "Herramientas", "Contenido", "Explicación"]
        
        self.preguntas = {
            "Actividades": [
                "¿Las actividades propuestas ayudaron a comprender mejor los conceptos de la materia? (1-10)",
                "¿Las actividades fueron desafiantes pero alcanzables? (1-10)",
                "¿Las actividades estuvieron bien distribuidas a lo largo del curso? (1-10)"
            ],
            "Herramientas": [
                "¿Las herramientas utilizadas en la asignatura fueron apropiadas para los objetivos del curso? (1-10)",
                "¿Tuviste suficiente acceso a las herramientas necesarias durante el curso? (1-10)",
                "¿La interfaz de las herramientas utilizadas fue fácil de usar? (1-10)"
            ],
            "Contenido": [
                "¿El contenido de la asignatura fue claro y bien explicado? (1-10)",
                "¿El contenido de la asignatura cubrió todos los temas relevantes de la materia? (1-10)",
                "¿El contenido fue relevante para tus estudios y tu futura carrera? (1-10)"
            ],
            "Explicación": [
                "¿El profesor explicó los temas de manera clara y comprensible? (1-10)",
                "¿El profesor fomentó la participación activa durante las clases? (1-10)",
                "¿El profesor resolvió tus dudas de manera efectiva? (1-10)"
            ]
        }

        self.entradas = {aspecto: [] for aspecto in self.aspectos}
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="PROGRAMACIÓN LÓGICA Y FUNCIONAL", font=("Helvetica", 14, "bold")).grid(row=0, columnspan=2, pady=(10, 0))
        tk.Label(self.root, text="Ingrese su calificación del 1 al 10 para cada aspecto").grid(row=1, columnspan=2, pady=10)

        def crear_preguntas_recursivas(fila, aspectos):
            if not aspectos:
                return fila
            aspecto = aspectos[0]
            tk.Label(self.root, text=aspecto, font=("Arial", 12, "bold")).grid(row=fila, columnspan=2, pady=(10, 0))
            fila += 1
            def crear_pregunta_recursiva(fila, preguntas):
                if not preguntas:
                    return fila
                tk.Label(self.root, text=preguntas[0]).grid(row=fila, column=0, sticky="w", padx=10)
                entrada = tk.Entry(self.root)
                entrada.grid(row=fila, column=1, padx=10)
                self.entradas[aspecto].append(entrada)
                return crear_pregunta_recursiva(fila + 1, preguntas[1:])
            fila = crear_pregunta_recursiva(fila, self.preguntas[aspecto])
            return crear_preguntas_recursivas(fila, aspectos[1:])

        fila_boton = crear_preguntas_recursivas(2, self.aspectos)
        tk.Button(self.root, text="Enviar Respuesta", command=self.enviar_respuesta).grid(row=fila_boton+1, columnspan=2, pady=10)
        tk.Button(self.root, text="Ver Resultados", command=self.ver_resultados).grid(row=fila_boton+2, columnspan=2, pady=10)
        tk.Button(self.root, text="Ver gráfica de promedios", command=self.ver_grafica_promedios).grid(row=fila_boton+3, columnspan=2, pady=10)

    def enviar_respuesta(self):
        try:
            def obtener_respuestas(aspectos):
                if not aspectos:
                    return {}
                aspecto = aspectos[0]
                respuestas = map_recursivo(lambda entrada: int(entrada.get()), self.entradas[aspecto])
                return {aspecto: respuestas} | obtener_respuestas(aspectos[1:])

            respuestas = obtener_respuestas(self.aspectos)

            def validar_todas_respuestas(aspectos):
                if not aspectos:
                    return True
                return validar_respuestas_recursivas(respuestas[aspectos[0]]) and validar_todas_respuestas(aspectos[1:])

            if not validar_todas_respuestas(self.aspectos):
                raise ValueError("Las calificaciones deben estar entre 1 y 10.")

            respuestas_acumuladas.append(respuestas)
            alumno_id = len(respuestas_acumuladas)
            promedios = map_recursivo(lambda aspecto: calcular_promedio(respuestas[aspecto]), self.aspectos)
            promedio = calcular_promedio(promedios)
            messagebox.showinfo("Respuesta registrada", f"Gracias Alumno {alumno_id}. Promedio: {promedio}")
            map_recursivo(lambda entrada: entrada.delete(0, tk.END), [entrada for entradas in self.entradas.values() for entrada in entradas])

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese calificaciones válidas (números entre 1 y 10).")

    def ver_resultados(self):
        if not respuestas_acumuladas:
            messagebox.showinfo("Sin datos", "Aún no hay respuestas registradas.")
            return

        def calcular_promedios_individuales_recursivos(respuestas, index):
            if index == len(respuestas):
                return []
            alumno = respuestas[index]

            def obtener_calificaciones(aspectos):
                if not aspectos:
                    return []
                return alumno[aspectos[0]] + obtener_calificaciones(aspectos[1:])

            calificaciones = obtener_calificaciones(list(alumno.keys()))
            return [calcular_promedio(calificaciones)] + calcular_promedios_individuales_recursivos(respuestas, index + 1)

        promedios_individuales = calcular_promedios_individuales_recursivos(respuestas_acumuladas, 0)
        resultado_texto = "Promedios individuales:\n"
        resultado_texto += "".join([f"Alumno {i+1}: Promedio de calificaciones: {promedio}\n" for i, promedio in enumerate(promedios_individuales)])
        todas = [calificacion for alumno in respuestas_acumuladas for aspecto in alumno.values() for calificacion in aspecto]
        promedio_general = calcular_promedio(todas)
        resultado_texto += f"\nPromedio general de todas las encuestas: {promedio_general:.1f}"
        messagebox.showinfo("Promedios individuales y general", resultado_texto)

    def ver_grafica_promedios(self):
        if not respuestas_acumuladas:
            messagebox.showinfo("Sin datos", "Aún no hay respuestas registradas.")
            return

        def calcular_promedios_recursivos(respuestas, index):
            if index == len(respuestas):
                return []
            alumno = respuestas[index]

            def obtener_calificaciones(aspectos):
                if not aspectos:
                    return []
                return alumno[aspectos[0]] + obtener_calificaciones(aspectos[1:])

            calificaciones = obtener_calificaciones(list(alumno.keys()))
            return [calcular_promedio(calificaciones)] + calcular_promedios_recursivos(respuestas, index + 1)

        promedios = calcular_promedios_recursivos(respuestas_acumuladas, 0)
        alumnos = [f"Alumno{i+1}" for i in range(len(promedios))]
        promedio_general = calcular_promedio(promedios)

        plt.figure(figsize=(8, 5))
        plt.bar(alumnos, promedios, color='mediumseagreen')
        plt.axhline(promedio_general, color='red', linestyle='--', label=f'Promedio general: {promedio_general:.1f}')
        plt.ylim(0, 10)
        plt.title("Promedio individual por alumno\n(con promedio general proyectado)")
        plt.ylabel("Promedio individual")
        plt.xlabel("----------ALUMNOS INSCRITOS EN LA MATERIA----------")
        plt.legend()
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = EncuestaApp(root)
    root.mainloop()
