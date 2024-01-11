import json
from Generos import cargar_base_datosgeneros, listargeneros
from Actores import cargar_base_datosactores, listaractores, guardar_base_de_datos_actores
from Formatos import cargar_base_datosformatos, listaformatos

def cargar_base_datos_peliculas():
    try:
        with open("Peliculas.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"peliculas": {}, "genero": {}, "actores": [], "formatos": []}
    return data

def guardar_base_datos(data):
    with open("Peliculas.json", "w") as file:
        json.dump(data, file, indent=2)

def obtener_nombre_genero(id_genero, datageneros):
    for item in datageneros["genero"]:
        if isinstance(item, list):
            if item[0]["id"] == id_genero:
                return item[0]["nombre"]
        elif isinstance(item, dict):
            if item["id"] == id_genero:
                return item["nombre"]
    return None

def obtener_nombre_actor(id_actor, datactores):
    for item in datactores["actor"]:
        if isinstance(item,list):
            if item[0]["id"] == id_actor:
                return item[0]["nombre"]
        elif isinstance(item, dict):
            if item["id"] == id_actor:
                return item["nombre"]
    return None

def obtener_nombre_formato(id_formato, dataformato):
    for item in dataformato["formato"]:
        if isinstance(item, list):
            if item[0]["id"] == id_formato:
                return item[0]["nombre"]
        elif isinstance (item, dict):
            if item["id"] == id_formato:
                return item["nombre"]
    return None

def agregarpelicula():
    data = cargar_base_datos_peliculas()
    datageneros = cargar_base_datosgeneros()
    dataactores= cargar_base_datosactores()
    dataformato= cargar_base_datosformatos()

    id_pelicula = input("Ingrese el ID de la película: ")
    nombre_pelicula = input("Ingrese el nombre de la película: ")
    duracion_pelicula = input("Ingrese la duración de la película: ")
    sinopsis_pelicula = input("Ingrese la sinopsis de la película: ")
    listargeneros()  
    id_genero = input("Ingrese el ID del género: ")
    listaractores()
    id_actor= input("Ingrese el ID del actor: ")
    listaformatos()
    id_formato= input ("Ingrese el ID del formato: ")



    nombre_genero = obtener_nombre_genero(id_genero, datageneros)
    nombre_actor = obtener_nombre_actor(id_actor, dataactores)
    nombre_formato = obtener_nombre_formato(id_formato, dataformato)

    if nombre_genero:
        pelicula = {
            "id": id_pelicula,
            "nombre": nombre_pelicula,
            "duracion": duracion_pelicula,
            "sinopsis": sinopsis_pelicula,
            "genero": {
                "id": id_genero,
                "nombre": nombre_genero
            }
        }
        data["peliculas"][id_pelicula] = pelicula
        guardar_base_datos(data)
        print("Película agregada exitosamente.")
    else:
        print("ID de género no válido. Por favor, elija un ID de género existente.")

    if nombre_actor:
        pelicula = {
            "id": id_pelicula,
            "nombre": nombre_pelicula,
            "duracion": duracion_pelicula,
            "sinopsis": sinopsis_pelicula,
            "genero": {
                "id": id_genero,
                "nombre": nombre_genero
            },
            "actor": {
                "id": id_actor,
                "nombre": nombre_actor
            }
        }
    
    if nombre_formato:
        pelicula = {
            "id": id_pelicula,
            "nombre": nombre_pelicula,
            "duracion": duracion_pelicula,
            "sinopsis": sinopsis_pelicula,
            "genero": {
                "id": id_genero,
                "nombre": nombre_genero
            },
            "actor": {
                "id": id_actor,
                "nombre": nombre_actor
            },
            "formato": {
                "id": id_formato,
                "nombre": nombre_formato
            }
        } 

def editarpelicula():
    data = cargar_base_datos_peliculas()
    datageneros = cargar_base_datosgeneros()
    dataactores = cargar_base_datosactores()
    dataformato = cargar_base_datosformatos()

    id_pelicula_a_editar = input("Ingrese el ID de la película que desea editar: ")

    if id_pelicula_a_editar in data["peliculas"]:
        pelicula_existente = data["peliculas"][id_pelicula_a_editar]
        print(f"Editando información para la película con ID {id_pelicula_a_editar}:")
        print(f"Nombre actual: {pelicula_existente['nombre']}")
        nuevo_nombre = input("Ingrese el nuevo nombre de la película (o presione Enter para dejarlo igual): ").strip() or pelicula_existente['nombre']
        nuevo_duracion = input("Ingrese la nueva duración de la película (o presione Enter para dejarla igual): ").strip() or pelicula_existente['duracion']
        nueva_sinopsis = input("Ingrese la nueva sinopsis de la película (o presione Enter para dejarla igual): ").strip() or pelicula_existente['sinopsis']

        print("Lista de géneros disponibles:")
        listargeneros()
        nuevo_id_genero = input("Ingrese el nuevo ID del género (o presione Enter para dejarlo igual): ").strip() or pelicula_existente['genero']['id']
        nuevo_nombre_genero = obtener_nombre_genero(nuevo_id_genero, datageneros) or pelicula_existente['genero']['nombre']

        print("Lista de actores disponibles:")
        listaractores()
        nuevo_id_actor = input("Ingrese el nuevo ID del actor (o presione Enter para dejarlo igual): ").strip() or (pelicula_existente['actor']['id'] if 'actor' in pelicula_existente else '')
        nuevo_nombre_actor = obtener_nombre_actor(nuevo_id_actor, dataactores) or (pelicula_existente['actor']['nombre'] if 'actor' in pelicula_existente else '')

        print("Lista de formatos disponibles:")
        listaformatos()
        nuevo_id_formato = input("Ingrese el nuevo ID del formato (o presione Enter para dejarlo igual): ").strip() or (pelicula_existente['formato']['id'] if 'formato' in pelicula_existente else '')
        nuevo_nombre_formato = obtener_nombre_formato(nuevo_id_formato, dataformato) or (pelicula_existente['formato']['nombre'] if 'formato' in pelicula_existente else '')

        pelicula_editada = {
            "id": id_pelicula_a_editar,
            "nombre": nuevo_nombre,
            "duracion": nuevo_duracion,
            "sinopsis": nueva_sinopsis,
            "genero": {
                "id": nuevo_id_genero,
                "nombre": nuevo_nombre_genero
            },
            "actor": {
                "id": nuevo_id_actor,
                "nombre": nuevo_nombre_actor
            } if nuevo_id_actor else None,
            "formato": {
                "id": nuevo_id_formato,
                "nombre": nuevo_nombre_formato
            } if nuevo_id_formato else None
        }

        data["peliculas"][id_pelicula_a_editar] = pelicula_editada
        guardar_base_datos(data)
        print(f"Película con ID {id_pelicula_a_editar} editada exitosamente.")
    else:
        print(f"No existe ninguna película con el ID {id_pelicula_a_editar}.")

def eliminarpelicula():
    data = cargar_base_datos_peliculas()

    id_pelicula_a_eliminar = input("Ingrese el ID de la película que desea eliminar: ")

    if id_pelicula_a_eliminar in data["peliculas"]:
        pelicula_eliminada = data["peliculas"].pop(id_pelicula_a_eliminar)
        guardar_base_datos(data)
        print(f"Película con ID {id_pelicula_a_eliminar} eliminada exitosamente:")
        print(f"Nombre: {pelicula_eliminada['nombre']}")
        print(f"Género: {pelicula_eliminada['genero']['nombre']}")
        print(f"Duración: {pelicula_eliminada['duracion']}")
        print(f"Sinopsis: {pelicula_eliminada['sinopsis']}")
        print(f"Actor: {pelicula_eliminada['actor']['nombre']}" if 'actor' in pelicula_eliminada else "Actor: No especificado")
        print(f"Formato: {pelicula_eliminada['formato']['nombre']}" if 'formato' in pelicula_eliminada else "Formato: No especificado")
    else:
        print(f"No existe ninguna película con el ID {id_pelicula_a_eliminar}.")

def eliminaractor():
    dataactores = cargar_base_datosactores()

    id_actor_a_eliminar = input("Ingrese el ID del actor que desea eliminar: ")

    if id_actor_a_eliminar in dataactores["actor"]:
        actor_eliminado = dataactores["actor"].pop(id_actor_a_eliminar)
        guardar_base_de_datos_actores(dataactores)
        print(f"Actor con ID {id_actor_a_eliminar} eliminado exitosamente:")
        print(f"Nombre: {actor_eliminado['nombre']}")
        print(f"Edad: {actor_eliminado['edad']}")
        print(f"Sexo: {actor_eliminado['sexo']}")
        print(f"Nacionalidad: {actor_eliminado['nacionalidad']}")
    else:
        print(f"No existe ningún actor con el ID {id_actor_a_eliminar}.")

def buscar_pelicula_por_id():
    data = cargar_base_datos_peliculas()

    id_pelicula_a_buscar = input("Ingrese el ID de la película que desea buscar: ")

    if id_pelicula_a_buscar in data["peliculas"]:
        pelicula = data["peliculas"][id_pelicula_a_buscar]
        print(f"Detalles de la película con ID {id_pelicula_a_buscar}:")
        print(f"Nombre: {pelicula['nombre']}")
        print(f"Género: {pelicula['genero']['nombre']}")
        print(f"Duración: {pelicula['duracion']}")
        print(f"Sinopsis: {pelicula['sinopsis']}")
        print(f"Actor: {pelicula['actor']['nombre']}" if 'actor' in pelicula else "Actor: No especificado")
        print(f"Formato: {pelicula['formato']['nombre']}" if 'formato' in pelicula else "Formato: No especificado")
    else:
        print(f"No existe ninguna película con el ID {id_pelicula_a_buscar}.")

def listar_todas_las_peliculas():
    data = cargar_base_datos_peliculas()

    if data["peliculas"]:
        print("Listado de todas las películas:")
        for id_pelicula, pelicula in data["peliculas"].items():
            print(f"ID: {id_pelicula}")
            print(f"Nombre: {pelicula['nombre']}")
            print(f"Género: {pelicula['genero']['nombre']}")
            print(f"Duración: {pelicula['duracion']}")
            print(f"Sinopsis: {pelicula['sinopsis']}")
            print(f"Actor: {pelicula['actor']['nombre']}" if 'actor' in pelicula else "Actor: No especificado")
            print(f"Formato: {pelicula['formato']['nombre']}" if 'formato' in pelicula else "Formato: No especificado")
            print("-" * 30)
    else:
        print("No hay películas registradas.")