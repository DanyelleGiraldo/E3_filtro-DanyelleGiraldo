from Peliculas import cargar_base_datos_peliculas
from Generos import listargeneros
from Actores import listaractores, cargar_base_datosactores

def listar_peliculas_por_genero():
    data = cargar_base_datos_peliculas()

    # Mostrar la lista de géneros disponibles
    print("Listado de géneros registrados:")
    listargeneros()

    genero_id = input("Ingrese el ID del género para listar sus películas: ")

    if genero_id in data["genero"]:
        nombre_genero = data["genero"][genero_id]["nombre"]
        peliculas_del_genero = [pelicula for pelicula in data["peliculas"].values() if pelicula["genero"]["id"] == genero_id]

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
    data = cargar_base_datos_peliculas()

    # Mostrar la lista de actores disponibles
    print("Listado de actores registrados:")
    listaractores()

    actor_id = input("Ingrese el ID del actor para listar las películas en las que ha participado: ")

    if actor_id in cargar_base_datosactores["actor"]:
        nombre_actor = cargar_base_datosactores["actor"][actor_id]["nombre"]
        peliculas_del_actor = [pelicula for pelicula in data["peliculas"].values() if 'actor' in pelicula and pelicula['actor']['id'] == actor_id]

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

