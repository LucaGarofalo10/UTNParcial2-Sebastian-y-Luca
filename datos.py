barra_total = 40  # Largo total de la barra
tiempo_barra = 10  # Segundos que tarda en vaciarse la barra
preguntas = [
    # CIENCIA
    {"categoria": "Ciencia", "dificultad": "Fácil", "pregunta": "¿Qué planeta es conocido como el planeta rojo?", "respuestas": ["Marte", "Júpiter", "Venus"], "correcta": 0},
    {"categoria": "Ciencia", "dificultad": "Fácil", "pregunta": "¿Cuál es el estado del agua a 0°C?", "respuestas": ["Sólido", "Líquido", "Gas"], "correcta": 0},
    {"categoria": "Ciencia", "dificultad": "Fácil", "pregunta": "¿Qué gas respiramos principalmente?", "respuestas": ["Oxígeno", "Hidrógeno", "Nitrógeno"], "correcta": 2},
    {"categoria": "Ciencia", "dificultad": "Fácil", "pregunta": "¿Cuál es el hueso más largo del cuerpo humano?", "respuestas": ["Fémur", "Radio", "Húmero"], "correcta": 0},
    {"categoria": "Ciencia", "dificultad": "Fácil", "pregunta": "¿Qué órgano bombea sangre?", "respuestas": ["Corazón", "Pulmón", "Hígado"], "correcta": 0},

    {"categoria": "Ciencia", "dificultad": "Normal", "pregunta": "¿Cuántos elementos hay en la tabla periódica?", "respuestas": ["118", "112", "100"], "correcta": 0},
    {"categoria": "Ciencia", "dificultad": "Normal", "pregunta": "¿Qué tipo de energía produce el Sol?", "respuestas": ["Nuclear", "Térmica", "Cinética"], "correcta": 0},
    {"categoria": "Ciencia", "dificultad": "Normal", "pregunta": "¿Qué científico desarrolló la teoría de la relatividad?", "respuestas": ["Einstein", "Newton", "Tesla"], "correcta": 0},
    {"categoria": "Ciencia", "dificultad": "Normal", "pregunta": "¿Qué parte de la célula contiene el ADN?", "respuestas": ["Núcleo", "Citoplasma", "Mitocondria"], "correcta": 0},
    {"categoria": "Ciencia", "dificultad": "Normal", "pregunta": "¿Cuál es la fórmula química del agua?", "respuestas": ["H2O", "CO2", "NaCl"], "correcta": 0},

    {"categoria": "Ciencia", "dificultad": "Difícil", "pregunta": "¿Qué partícula subatómica tiene carga positiva?", "respuestas": ["Protón", "Neutrón", "Electrón"], "correcta": 0},
    {"categoria": "Ciencia", "dificultad": "Difícil", "pregunta": "¿Qué ley describe la gravedad?", "respuestas": ["Ley de Newton", "Ley de Faraday", "Ley de Ohm"], "correcta": 0},
    {"categoria": "Ciencia", "dificultad": "Difícil", "pregunta": "¿Qué científico descubrió la penicilina?", "respuestas": ["Fleming", "Darwin", "Curie"], "correcta": 0},
    {"categoria": "Ciencia", "dificultad": "Difícil", "pregunta": "¿Qué unidad mide la intensidad de corriente?", "respuestas": ["Amperio", "Voltio", "Ohmio"], "correcta": 0},
    {"categoria": "Ciencia", "dificultad": "Difícil", "pregunta": "¿Qué planeta tiene un día más largo que su año?", "respuestas": ["Venus", "Saturno", "Mercurio"], "correcta": 0},

    # HISTORIA
    {"categoria": "Historia", "dificultad": "Fácil", "pregunta": "¿Quién fue el primer presidente de Argentina?", "respuestas": ["Rivadavia", "Belgrano", "San Martín"], "correcta": 0},
    {"categoria": "Historia", "dificultad": "Fácil", "pregunta": "¿En qué año fue la Revolución de Mayo?", "respuestas": ["1810", "1816", "1806"], "correcta": 0},
    {"categoria": "Historia", "dificultad": "Fácil", "pregunta": "¿De qué país era Napoleón?", "respuestas": ["Francia", "España", "Italia"], "correcta": 0},
    {"categoria": "Historia", "dificultad": "Fácil", "pregunta": "¿Cuál fue la causa de la Segunda Guerra Mundial?", "respuestas": ["Invasión a Polonia", "Muerte de un archiduque", "Colonialismo"], "correcta": 0},
    {"categoria": "Historia", "dificultad": "Fácil", "pregunta": "¿Quién escribió el Martín Fierro?", "respuestas": ["José Hernández", "Sarmiento", "Rosas"], "correcta": 0},

    {"categoria": "Historia", "dificultad": "Normal", "pregunta": "¿Quién descubrió América?", "respuestas": ["Cristóbal Colón", "Américo Vespucio", "Magallanes"], "correcta": 0},
    {"categoria": "Historia", "dificultad": "Normal", "pregunta": "¿Qué imperio construyó el Coliseo?", "respuestas": ["Romano", "Griego", "Egipcio"], "correcta": 0},
    {"categoria": "Historia", "dificultad": "Normal", "pregunta": "¿Qué país fue dividido por el Muro de Berlín?", "respuestas": ["Alemania", "Austria", "Polonia"], "correcta": 0},
    {"categoria": "Historia", "dificultad": "Normal", "pregunta": "¿Quién fue Juana de Arco?", "respuestas": ["Heroína francesa", "Reina inglesa", "Emperatriz romana"], "correcta": 0},
    {"categoria": "Historia", "dificultad": "Normal", "pregunta": "¿Qué guerra terminó en 1945?", "respuestas": ["Segunda Guerra Mundial", "Primera Guerra Mundial", "Guerra Fría"], "correcta": 0},

    {"categoria": "Historia", "dificultad": "Difícil", "pregunta": "¿Qué tratado puso fin a la Primera Guerra Mundial?", "respuestas": ["Tratado de Versalles", "Tratado de París", "Tratado de Viena"], "correcta": 0},
    {"categoria": "Historia", "dificultad": "Difícil", "pregunta": "¿En qué año cayó el Imperio Romano de Occidente?", "respuestas": ["476", "1492", "1066"], "correcta": 0},
    {"categoria": "Historia", "dificultad": "Difícil", "pregunta": "¿Qué revolución ocurrió en 1917?", "respuestas": ["Rusa", "Francesa", "Industrial"], "correcta": 0},
    {"categoria": "Historia", "dificultad": "Difícil", "pregunta": "¿Quién fue Ramsés II?", "respuestas": ["Faraón egipcio", "Rey babilonio", "Emperador griego"], "correcta": 0},
    {"categoria": "Historia", "dificultad": "Difícil", "pregunta": "¿Qué país inició la Reforma Protestante?", "respuestas": ["Alemania", "Inglaterra", "Italia"], "correcta": 0},

    # ENTRETENIMIENTO
    {"categoria": "Entretenimiento", "dificultad": "Fácil", "pregunta": "¿Quién es el protagonista de Harry Potter?", "respuestas": ["Harry Potter", "Ron Weasley", "Hermione Granger"], "correcta": 0},
    {"categoria": "Entretenimiento", "dificultad": "Fácil", "pregunta": "¿Qué personaje es amarillo y vive en una piña?", "respuestas": ["Bob Esponja", "Homero", "Minion"], "correcta": 0},
    {"categoria": "Entretenimiento", "dificultad": "Fácil", "pregunta": "¿Qué saga tiene un anillo único?", "respuestas": ["El Señor de los Anillos", "Star Wars", "Harry Potter"], "correcta": 0},
    {"categoria": "Entretenimiento", "dificultad": "Fácil", "pregunta": "¿Quién canta 'Thriller'?", "respuestas": ["Michael Jackson", "Elvis Presley", "Madonna"], "correcta": 0},
    {"categoria": "Entretenimiento", "dificultad": "Fácil", "pregunta": "¿Qué videojuego tiene a Mario como personaje?", "respuestas": ["Super Mario", "Zelda", "Minecraft"], "correcta": 0},

    {"categoria": "Entretenimiento", "dificultad": "Normal", "pregunta": "¿Quién dirigió 'Titanic'?", "respuestas": ["James Cameron", "Steven Spielberg", "Peter Jackson"], "correcta": 0},
    {"categoria": "Entretenimiento", "dificultad": "Normal", "pregunta": "¿Qué serie tiene dragones y tronos?", "respuestas": ["Game of Thrones", "Vikings", "The Witcher"], "correcta": 0},
    {"categoria": "Entretenimiento", "dificultad": "Normal", "pregunta": "¿Qué película tiene a Thanos como villano?", "respuestas": ["Avengers", "Iron Man", "Thor"], "correcta": 0},
    {"categoria": "Entretenimiento", "dificultad": "Normal", "pregunta": "¿Cuál es el apellido de Sherlock?", "respuestas": ["Holmes", "Watson", "Moriarty"], "correcta": 0},
    {"categoria": "Entretenimiento", "dificultad": "Normal", "pregunta": "¿Qué personaje usa una espada láser?", "respuestas": ["Luke Skywalker", "Neo", "Bilbo"], "correcta": 0},

    {"categoria": "Entretenimiento", "dificultad": "Difícil", "pregunta": "¿Qué actor interpretó a Gandalf?", "respuestas": ["Ian McKellen", "Patrick Stewart", "Anthony Hopkins"], "correcta": 0},
    {"categoria": "Entretenimiento", "dificultad": "Difícil", "pregunta": "¿Quién ganó el Oscar a mejor película en 2020?", "respuestas": ["Parasite", "1917", "Joker"], "correcta": 0},
    {"categoria": "Entretenimiento", "dificultad": "Difícil", "pregunta": "¿Qué director hizo 'Pulp Fiction'?", "respuestas": ["Tarantino", "Scorsese", "Kubrick"], "correcta": 0},
    {"categoria": "Entretenimiento", "dificultad": "Difícil", "pregunta": "¿Qué banda compuso 'Bohemian Rhapsody'?", "respuestas": ["Queen", "The Beatles", "Pink Floyd"], "correcta": 0},
    {"categoria": "Entretenimiento", "dificultad": "Difícil", "pregunta": "¿En qué año salió el primer PlayStation?", "respuestas": ["1994", "1999", "2001"], "correcta": 0},
]
