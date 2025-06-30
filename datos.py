barra_total = 40  # Largo total de la barra
dificultad_facil = 14
dificultad_normal = 10
dificultad_dificil = 8
preguntas = [
    # CIENCIA
    {"categoria": "Ciencia", "dificultad": "Fácil", "pregunta": "¿Qué planeta es conocido como el planeta rojo?", "respuestas": ["Venus", "Júpiter", "Marte"], "correcta": 2},
    {"categoria": "Ciencia", "dificultad": "Fácil", "pregunta": "¿Cuál es el estado del agua a 0°C?", "respuestas": ["Líquido", "Gas", "Sólido"], "correcta": 2},
    {"categoria": "Ciencia", "dificultad": "Fácil", "pregunta": "¿Qué gas respiramos principalmente?", "respuestas": ["Oxígeno", "Nitrógeno", "Hidrógeno"], "correcta": 1},
    {"categoria": "Ciencia", "dificultad": "Fácil", "pregunta": "¿Cuál es el hueso más largo del cuerpo humano?", "respuestas": ["Radio", "Fémur", "Húmero"], "correcta": 1},
    {"categoria": "Ciencia", "dificultad": "Fácil", "pregunta": "¿Qué órgano bombea sangre?", "respuestas": ["Corazón", "Hígado", "Pulmón"], "correcta": 0},

    {"categoria": "Ciencia", "dificultad": "Normal", "pregunta": "¿Cuántos elementos hay en la tabla periódica?", "respuestas": ["112", "118", "100"], "correcta": 1},
    {"categoria": "Ciencia", "dificultad": "Normal", "pregunta": "¿Qué tipo de energía produce el Sol?", "respuestas": ["Nuclear", "Cinética", "Térmica"], "correcta": 0},
    {"categoria": "Ciencia", "dificultad": "Normal", "pregunta": "¿Qué científico desarrolló la teoría de la relatividad?", "respuestas": ["Tesla", "Newton", "Einstein"], "correcta": 2},
    {"categoria": "Ciencia", "dificultad": "Normal", "pregunta": "¿Qué parte de la célula contiene el ADN?", "respuestas": ["Mitocondria", "Citoplasma", "Núcleo"], "correcta": 2},
    {"categoria": "Ciencia", "dificultad": "Normal", "pregunta": "¿Cuál es la fórmula química del agua?", "respuestas": ["NaCl", "CO2", "H2O"], "correcta": 2},

    {"categoria": "Ciencia", "dificultad": "Difícil", "pregunta": "¿Qué partícula subatómica tiene carga positiva?", "respuestas": ["Neutrón", "Protón", "Electrón"], "correcta": 1},
    {"categoria": "Ciencia", "dificultad": "Difícil", "pregunta": "¿Qué ley describe la gravedad?", "respuestas": ["Ley de Faraday", "Ley de Newton", "Ley de Ohm"], "correcta": 1},
    {"categoria": "Ciencia", "dificultad": "Difícil", "pregunta": "¿Qué científico descubrió la penicilina?", "respuestas": ["Fleming", "Darwin", "Curie"], "correcta": 0},
    {"categoria": "Ciencia", "dificultad": "Difícil", "pregunta": "¿Qué unidad mide la intensidad de corriente?", "respuestas": ["Voltio", "Ohmio", "Amperio"], "correcta": 2},
    {"categoria": "Ciencia", "dificultad": "Difícil", "pregunta": "¿Qué planeta tiene un día más largo que su año?", "respuestas": ["Venus", "Saturno", "Mercurio"], "correcta": 0},

    # HISTORIA
    {"categoria": "Historia", "dificultad": "Fácil", "pregunta": "¿Quién fue el primer presidente de Argentina?", "respuestas": ["San Martín", "Belgrano", "Rivadavia"], "correcta": 2},
    {"categoria": "Historia", "dificultad": "Fácil", "pregunta": "¿En qué año fue la Revolución de Mayo?", "respuestas": ["1816", "1806", "1810"], "correcta": 2},
    {"categoria": "Historia", "dificultad": "Fácil", "pregunta": "¿De qué país era Napoleón?", "respuestas": ["Italia", "Francia", "España"], "correcta": 1},
    {"categoria": "Historia", "dificultad": "Fácil", "pregunta": "¿Cuál fue la causa de la Segunda Guerra Mundial?", "respuestas": ["Invasión a Polonia", "Colonialismo", "Muerte de un archiduque"], "correcta": 0},
    {"categoria": "Historia", "dificultad": "Fácil", "pregunta": "¿Quién escribió el Martín Fierro?", "respuestas": ["Rosas", "Sarmiento", "José Hernández"], "correcta": 2},

    {"categoria": "Historia", "dificultad": "Normal", "pregunta": "¿Quién descubrió América?", "respuestas": ["Cristóbal Colón", "Magallanes", "Américo Vespucio"], "correcta": 0},
    {"categoria": "Historia", "dificultad": "Normal", "pregunta": "¿Qué imperio construyó el Coliseo?", "respuestas": ["Romano", "Griego", "Egipcio"], "correcta": 0},
    {"categoria": "Historia", "dificultad": "Normal", "pregunta": "¿Qué país fue dividido por el Muro de Berlín?", "respuestas": ["Austria", "Polonia", "Alemania"], "correcta": 2},
    {"categoria": "Historia", "dificultad": "Normal", "pregunta": "¿Quién fue Juana de Arco?", "respuestas": ["Heroína francesa", "Emperatriz romana", "Reina inglesa"], "correcta": 0},
    {"categoria": "Historia", "dificultad": "Normal", "pregunta": "¿Qué guerra terminó en 1945?", "respuestas": ["Primera Guerra Mundial", "Segunda Guerra Mundial", "Guerra Fría"], "correcta": 1},

    {"categoria": "Historia", "dificultad": "Difícil", "pregunta": "¿Qué tratado puso fin a la Primera Guerra Mundial?", "respuestas": ["Tratado de París", "Tratado de Viena", "Tratado de Versalles"], "correcta": 2},
    {"categoria": "Historia", "dificultad": "Difícil", "pregunta": "¿En qué año cayó el Imperio Romano de Occidente?", "respuestas": ["1066", "1492", "476"], "correcta": 2},
    {"categoria": "Historia", "dificultad": "Difícil", "pregunta": "¿Qué revolución ocurrió en 1917?", "respuestas": ["Industrial", "Francesa", "Rusa"], "correcta": 2},
    {"categoria": "Historia", "dificultad": "Difícil", "pregunta": "¿Quién fue Ramsés II?", "respuestas": ["Emperador griego", "Faraón egipcio", "Rey babilonio"], "correcta": 1},
    {"categoria": "Historia", "dificultad": "Difícil", "pregunta": "¿Qué país inició la Reforma Protestante?", "respuestas": ["Italia", "Alemania", "Inglaterra"], "correcta": 1},

    # ENTRETENIMIENTO
    {"categoria": "Entretenimiento", "dificultad": "Fácil", "pregunta": "¿Quién es el protagonista de Harry Potter?", "respuestas": ["Harry Potter", "Hermione Granger", "Ron Weasley"], "correcta": 0},
    {"categoria": "Entretenimiento", "dificultad": "Fácil", "pregunta": "¿Qué personaje es amarillo y vive en una piña?", "respuestas": ["Minion", "Homero", "Bob Esponja"], "correcta": 2},
    {"categoria": "Entretenimiento", "dificultad": "Fácil", "pregunta": "¿Qué saga tiene un anillo único?", "respuestas": ["El Señor de los Anillos", "Star Wars", "Harry Potter"], "correcta": 0},
    {"categoria": "Entretenimiento", "dificultad": "Fácil", "pregunta": "¿Quién canta 'Thriller'?", "respuestas": ["Michael Jackson", "Elvis Presley", "Madonna"], "correcta": 0},
    {"categoria": "Entretenimiento", "dificultad": "Fácil", "pregunta": "¿Qué videojuego tiene a Mario como personaje?", "respuestas": ["Super Mario", "Zelda", "Minecraft"], "correcta": 0},

    {"categoria": "Entretenimiento", "dificultad": "Normal", "pregunta": "¿Quién dirigió 'Titanic'?", "respuestas": ["Peter Jackson", "James Cameron", "Steven Spielberg"], "correcta": 1},
    {"categoria": "Entretenimiento", "dificultad": "Normal", "pregunta": "¿Qué serie tiene dragones y tronos?", "respuestas": ["The Witcher", "Vikings", "Game of Thrones"], "correcta": 2},
    {"categoria": "Entretenimiento", "dificultad": "Normal", "pregunta": "¿Qué película tiene a Thanos como villano?", "respuestas": ["Avengers", "Thor", "Iron Man"], "correcta": 0},
    {"categoria": "Entretenimiento", "dificultad": "Normal", "pregunta": "¿Cuál es el apellido de Sherlock?", "respuestas": ["Holmes", "Moriarty", "Watson"], "correcta": 0},
    {"categoria": "Entretenimiento", "dificultad": "Normal", "pregunta": "¿Qué personaje usa una espada láser?", "respuestas": ["Neo", "Bilbo", "Luke Skywalker"], "correcta": 2},

    {"categoria": "Entretenimiento", "dificultad": "Difícil", "pregunta": "¿Qué actor interpretó a Gandalf?", "respuestas": ["Ian McKellen", "Anthony Hopkins", "Patrick Stewart"], "correcta": 0},
    {"categoria": "Entretenimiento", "dificultad": "Difícil", "pregunta": "¿Quién ganó el Oscar a mejor película en 2020?", "respuestas": ["Joker", "Parasite", "1917"], "correcta": 1},
    {"categoria": "Entretenimiento", "dificultad": "Difícil", "pregunta": "¿Qué director hizo 'Pulp Fiction'?", "respuestas": ["Tarantino", "Kubrick", "Scorsese"], "correcta": 0},
    {"categoria": "Entretenimiento", "dificultad": "Difícil", "pregunta": "¿Qué banda compuso 'Bohemian Rhapsody'?", "respuestas": ["The Beatles", "Queen", "Pink Floyd"], "correcta": 1},
    {"categoria": "Entretenimiento", "dificultad": "Difícil", "pregunta": "¿En qué año salió el primer PlayStation?", "respuestas": ["1999", "2001", "1994"], "correcta": 2}
]

puntuaciones = []