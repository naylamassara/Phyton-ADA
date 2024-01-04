import random

 

palabras = ['amarillo', 'azul', 'blanco', 'gris', 'casa', 'cielo', 'claro', 'color', 'comida', 'correr',

    'corto', 'creer', 'cruzar', 'cuadro', 'cuerpo', 'dama', 'dado', 'dulce', 'edad', 'elefante',

    'empezar', 'encontrar', 'entender', 'escalar', 'escribir', 'espacio', 'esperar', 'estrella', 'estudiar', 'feliz',

    'flor', 'frutilla', 'fruta', 'fuego', 'gato', 'girar', 'grande', 'gelatina', 'guitarra', 'hablar',

    'hacer', 'hermano', 'hijo', 'historia', 'hora', 'huevo', 'idea', 'igual', 'jugar', 'largo',

    'leer', 'libro', 'luz', 'madre', 'mano', 'mar', 'mesa', 'mirar', 'mover', 'mujer',

    'naranja', 'negro', 'nueve', 'nube', 'ojo', 'oso', 'padre', 'piso', 'palabra', 'papel',

    'parar', 'paso', 'paz', 'pozo', 'perro', 'pez', 'pie', 'piedra', 'pintar', 'plata',

    'poder', 'pollo', 'prueba', 'punto', 'querer', 'roto', 'risa', 'reloj', 'rojo', 'rosa',

    'saber', 'sal', 'saltar', 'sentir', 'ser', 'silla', 'sol', 'sonreir', 'suave', 'subir',

    'taza', 'termo', 'temprano', 'tiempo', 'tigre', 'tomar', 'toro', 'trabajar', 'tres', 'ver',

    'verde', 'viaje', 'volar', 'volver', 'zapato', 'zorro', 'abrir', 'aceite', 'agua', 'alto',

    'amigo', 'animal', 'dinosaurio', 'arena', 'bajo', 'boca', 'brazo', 'cabeza', 'calor', 'cama',

    'campo', 'carne', 'ciudad', 'clase', 'clave', 'cocina', 'comer', 'copa', 'carro', 'cuerda',

    'dormir', 'duro', 'escuela', 'familia', 'fiesta', 'flaco', 'fuerza', 'gafas', 'gente', 'gracias',

    'hambre', 'hombre', 'invierno', 'foto', 'joven', 'juego', 'lago', 'lento', 'libre', 'llave',

    'lluvia', 'luna', 'madera', 'manzana', 'mariposa', 'mes', 'mono', 'mesa', 'nadar', 'nieve',

    'nuevo', 'oro', 'pan', 'pelo', 'piedra', 'piel', 'pluma', 'puerta', 'queso', 'rata',

    'ropa', 'sopa', 'tigre', 'torta', 'vaca', 'viento', 'vino', 'vivir', 'yerba', 'zumo']

 

palabra_aleatoria = random.choice(palabras)



intentos = 0

nueva_palabra = ['_'] * len(palabra_aleatoria)

 

print(f"La palabra que debe adivinar tiene estos casilleros {' '.join(nueva_palabra)}")

 

while intentos < 10 and '_' in nueva_palabra:

    entrada_usuario = input("Ingrese una letra: ")

 

    acertado = False

 

    for indice, x in enumerate(palabra_aleatoria):

        if entrada_usuario == x:

            nueva_palabra[indice] = entrada_usuario

            acertado = True

            print(f"La letra elegida es correcta y se encuentra en la posición {indice}")

 

    intentos += 1

 

    if not acertado:

        print(f"La letra es incorrecta. Usted tiene {10 - intentos} intentos restantes.")

 

    print(' '.join(nueva_palabra))

 

if '_' not in nueva_palabra:

    print(f"Felicidades, has adivinado la palabra {palabra_aleatoria}.")