from Peliculas import cargar_base_datos_peliculas, listar_todas_las_peliculas
from Generos import listargeneros, cargar_base_datosgeneros
from Actores import listaractores, cargar_base_datosactores

def obtener_nombre_genero(id_genero, datageneros):
    for item in datageneros:
        if isinstance(item, list):
            if item[0]["id"] == id_genero:
                return item[0]["nombre"]
        elif isinstance(item, dict):
            if item["id"] == id_genero:
                return item["nombre"]
    return None
def obtener_nombre_actor(id_actor, data_actores):
    for item in data_actores:
        if isinstance(item, list):
            if item[0]["id"] == id_actor:
                return item[0]["nombre"]
        elif isinstance(item, dict):
            if item["id"] == id_actor:
                return item["nombre"]
    return None

def listar_peliculas_por_genero():
    data_generos = cargar_base_datosgeneros()
    data_peliculas = cargar_base_datos_peliculas()

    
    print("Listado de géneros registrados:")
    listargeneros()

    genero_id = input("Ingrese el ID del género para listar sus películas: ")

    nombre_genero = obtener_nombre_genero(genero_id, data_generos["genero"])

    if nombre_genero:
        peliculas_del_genero = [pelicula for pelicula in data_peliculas["peliculas"].values() if pelicula["genero"]["id"] == genero_id]

        if peliculas_del_genero:
            print(f"\nListado de películas del género {nombre_genero}:")
            for pelicula in peliculas_del_genero:
                print(f"ID: {pelicula['id']}")
                print(f"Nombre: {pelicula['nombre']}")
                print(f"Duración: {pelicula['duracion']}")
                print(f"Sinopsis: {pelicula['sinopsis']}")
                print(f"Actor: {pelicula['actor']['nombre']}" if 'actor' in pelicula else "Actor: No especificado")
                print(f"Formato: {pelicula['formato']['nombre']}" if 'formato' in pelicula else "Formato: No especificado")
                print("-" * 30)
        else:
            print(f"No hay películas registradas para el género {nombre_genero}.")
    else:
        print("ID de género no válido. Por favor, elija un ID de género existente.")

def listar_peliculas_por_actor():
    data_actores = cargar_base_datosactores()
    data_peliculas = cargar_base_datos_peliculas()

    print("Listado de actores registrados:")
    listaractores()

    actor_id = input("Ingrese el ID del actor para listar las películas en las que ha participado: ")

    nombre_actor = obtener_nombre_actor(actor_id, data_actores["actor"])

    if nombre_actor:
        peliculas_del_actor = [pelicula for pelicula in data_peliculas["peliculas"].values() if 'actor' in pelicula and pelicula['actor']['id'] == actor_id]

        if peliculas_del_actor:
            print(f"\nListado de películas en las que ha participado {nombre_actor}:")
            for pelicula in peliculas_del_actor:
                print(f"ID: {pelicula['id']}")
                print(f"Nombre: {pelicula['nombre']}")
                print(f"Duración: {pelicula['duracion']}")
                print(f"Sinopsis: {pelicula['sinopsis']}")
                print(f"Género: {pelicula['genero']['nombre']}")
                print(f"Formato: {pelicula['formato']['nombre']}" if 'formato' in pelicula else "Formato: No especificado")
                print("-" * 30)
        else:
            print(f"No hay películas registradas con la participación del actor {nombre_actor}.")
    else:
        print("ID de actor no válido. Por favor, elija un ID de actor existente.")

def buscar_pelicula_por_id():
    data = cargar_base_datos_peliculas()
    listar_todas_las_peliculas()
    id_pelicula_a_buscar = input("Ingrese el ID de la película que desea buscar: ")

    if id_pelicula_a_buscar in data["peliculas"]:
        pelicula_encontrada = data["peliculas"][id_pelicula_a_buscar]
        nombre_actor = pelicula_encontrada['actor']['nombre'] if 'actor' in pelicula_encontrada else "No especificado"

        print("\nInformación de la película:")
        print(f"Nombre: {pelicula_encontrada['nombre']}")
        print(f"Sinopsis: {pelicula_encontrada['sinopsis']}")
        print(f"Actor: {nombre_actor}")
    else:
        print(f"No existe ninguna película con el ID {id_pelicula_a_buscar}.")

