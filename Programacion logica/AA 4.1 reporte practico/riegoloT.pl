% --- ASIGNACION DE ZONAS DESCRIPTIVAS ---
zona(zona1, 'Campo agricola').
zona(zona2, 'Jardin del edificio').
zona(zona3, 'Oficina principal').
zona(zona4, 'Casa residencial').
zona(zona5, 'Invernadero experimental').
zona(zona6, 'Terraza recreativa').

% --- HECHOS DE SENSOR POR ZONA ---

% humedad_suelo(Zona, Estado). Estado: baja, media, alta
humedad_suelo(zona1, baja).
humedad_suelo(zona2, media).
humedad_suelo(zona3, alta).
humedad_suelo(zona4, baja).
humedad_suelo(zona5, baja).
humedad_suelo(zona6, media).

% temperatura(Zona, Grados Celsius)
temperatura(zona1, 35).
temperatura(zona2, 28).
temperatura(zona3, 26).
temperatura(zona4, 33).
temperatura(zona5, 36).
temperatura(zona6, 30).

% pronostico_lluvia(Zona, LluviaEsperada). LluviaEsperada: true, false
pronostico_lluvia(zona1, false).
pronostico_lluvia(zona2, false).
pronostico_lluvia(zona3, true).
pronostico_lluvia(zona4, false).
pronostico_lluvia(zona5, false).
pronostico_lluvia(zona6, true).

% Hora del sistema
hora(20).

% --- REGLAS DE LOGICA ---

hora_adecuada :- 
    hora(H), 
    (H < 10 ; H > 18).

activar_riego(Zona) :- 
    humedad_suelo(Zona, baja),
    pronostico_lluvia(Zona, false),
    hora_adecuada.

estado_riego(Zona, 'Activado') :- activar_riego(Zona).
estado_riego(Zona, 'No activado') :- \+ activar_riego(Zona).

alerta_calor(Zona) :-
    temperatura(Zona, T),
    T >= 32.

estado_humedad :-
    forall(zona(Z, Nombre),
        (humedad_suelo(Z, Nivel),
         format('Zona: ~w (~w) -> Humedad del suelo: ~w~n', [Z, Nombre, Nivel]))).

recomendacion(Zona) :-
    zona(Zona, Nombre),
    activar_riego(Zona),
    temperatura(Zona, T),
    T >= 32, !,
    format('ALERTA: Zona ~w (~w) -> Riego activado bajo alta temperatura (~w C).~n', [Zona, Nombre, T]),
    format('Recomendacion: Utilizar riego nocturno o por goteo para evitar perdida de agua.~n').

recomendacion(Zona) :-
    zona(Zona, Nombre),
    activar_riego(Zona), !,
    format('Zona ~w (~w) -> Riego activado. No se detectaron condiciones criticas.~n', [Zona, Nombre]).

recomendacion(Zona) :-
    zona(Zona, Nombre),
    format('Zona ~w (~w) -> No se requiere riego por ahora.~n', [Zona, Nombre]).

recomendaciones_todas :-
    forall(zona(Z, _), recomendacion(Z)).
