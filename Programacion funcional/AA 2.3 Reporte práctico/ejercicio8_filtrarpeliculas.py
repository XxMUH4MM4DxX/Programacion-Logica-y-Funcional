lista_peliculas = [
    {
        "Titulo": "El Origen",
        "Año": "2010",
        "Clasificación": "PG-13",
        "Estreno": "16 Jul 2010",
        "Duración": "148 min",
        "Género": "Acción, Aventura, Crimen",
        "Director": "Christopher Nolan",
        "Guionista": "Christopher Nolan",
        "Actores": "Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page, Tom Hardy",
        "Trama": "Un ladrón que roba secretos corporativos mediante el uso de tecnología para compartir sueños recibe la tarea inversa de implantar una idea en la mente de un CEO.",
        "Idioma": "Inglés, Japonés, Francés",
        "País": "EE.UU., Reino Unido",
        "Premios": "Ganó 4 premios Oscar. Otros 143 premios y 198 nominaciones.",
        "Póster": "http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX300.jpg",
        "PuntajeMetascore": "74",
        "CalificaciónIMDB": "8.8",
        "VotosIMDB": "1,446,708",
        "IDIMDB": "tt1375666",
        "Tipo": "película",
        "Respuesta": "Verdadero"
    },
    {
        "Titulo": "Interestelar",
        "Año": "2014",
        "Clasificación": "PG-13",
        "Estreno": "07 Nov 2014",
        "Duración": "169 min",
        "Género": "Aventura, Drama, Ciencia Ficción",
        "Director": "Christopher Nolan",
        "Guionista": "Jonathan Nolan, Christopher Nolan",
        "Actores": "Ellen Burstyn, Matthew McConaughey, Mackenzie Foy, John Lithgow",
        "Trama": "Un equipo de exploradores viaja a través de un agujero de gusano en el espacio en un intento por asegurar la supervivencia de la humanidad.",
        "Idioma": "Inglés",
        "País": "EE.UU., Reino Unido",
        "Premios": "Ganó 1 premio Oscar. Otros 39 premios y 132 nominaciones.",
        "Póster": "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SX300.jpg",
        "PuntajeMetascore": "74",
        "CalificaciónIMDB": "8.6",
        "VotosIMDB": "910,366",
        "IDIMDB": "tt0816692",
        "Tipo": "película",
        "Respuesta": "Verdadero"
    }
]

# Filtrar películas con calificación IMDB mayor o igual a 8.0
mayor_a_8 = list(filter(lambda pelicula: float(pelicula["CalificaciónIMDB"]) >= 8.0, lista_peliculas))
print(mayor_a_8)  # Para verificar la lista filtrada

# Crear una nueva lista con solo el título y la calificación
nueva_lista = list(map(lambda pelicula: {"titulo": pelicula["Titulo"], "Calificacion": pelicula["CalificaciónIMDB"]}, mayor_a_8))
print(nueva_lista)  # Para verificar el mapeo correcto
