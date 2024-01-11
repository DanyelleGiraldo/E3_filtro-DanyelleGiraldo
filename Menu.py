import os
from Generos import Creargenero, listargeneros
from Actores import crearactor, listaractores
from Formatos import crearformato, listaformatos
from Peliculas import (
    agregarpelicula, editarpelicula, eliminarpelicula, eliminaractor,
    buscar_pelicula_por_id, listar_todas_las_peliculas
)
from Gestor_de_Informes import (
    listar_peliculas_por_genero, listar_peliculas_por_actor, buscar_pelicula_por_id
)

def mostrar_menu():
    while True:
        print("1. Administrador de generos")
        print("2. Administrador de Actores")
        print("3. Administrador de Formatos")
        print("4. Gestor de informes")
        print("5. Gestor de peliculas")
        print("6. Salir")
        op = input("Seleccione su opcion: ").strip()

        if op == "1":
            submenugeneros()
        elif op == "2":
            submenuactores()
            pass
        elif op == "3":
            gestorformatos()
            pass
        elif op == "4":
            submenuinformes()
            pass
        elif op == "5":
            gestorpeliculas()
            pass
        elif op == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def submenugeneros():
    while True:
        print("1. Crear genero")
        print("2. Listar generos")
        print("3. Volver al menú principal")
        opgenero = input("Seleccione su opcion: ").strip()

        if opgenero == "1":
            Creargenero()
        elif opgenero == "2":
            listargeneros()
        elif opgenero == "3":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opcion no valida")

def submenuactores():
    while True:
        print("1. Crear actor")
        print("2. Listar actores")
        print("3. Volver al menú principal")
        opactor = input("Seleccione su opcion: ").strip()

        if opactor == "1":
            crearactor()
        elif opactor == "2":
            listaractores()
        elif opactor == "3":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opcion no valida")

def gestorformatos():
    while True:
        print("1. Crear formatos")
        print("2. Listar formatos")
        print("3. Volver al menú principal")
        opactor = input("Seleccione su opcion: ").strip()

        if opactor == "1":
            crearformato()
        elif opactor == "2":
            listaformatos()
        elif opactor == "3":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opcion no valida")

def gestorpeliculas():
    while True:
        print("1. Agregar pelicula")
        print("2. Editar pelicula.")
        print("3. Eliminar pelicula.")
        print("4. Eliminar Actor.")
        print("5. Buscar pelicula.")
        print("6. Listar todas las peliculas")
        print("7. Volver al menú principal")
        oppeliculas = input("Seleccione su opcion: ").strip()

        if oppeliculas == "1":
            agregarpelicula()
        elif oppeliculas == "2":
            editarpelicula()
        elif oppeliculas == "3":
            eliminarpelicula()
        elif oppeliculas == "4":
            eliminaractor()
        elif oppeliculas == "5":
            buscar_pelicula_por_id()
        elif oppeliculas == "6":
            listar_todas_las_peliculas()
        elif oppeliculas == "7":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida")

def submenuinformes():
    while True:
        print("1. Listar las peliculas de un genero especifico.")
        print("2. Listar las peliculas por protagonista")
        print("3. Buscar pelicula y mostrar la sinopsis y actores")
        print("4. ir al menu principal")
        opactor = input("Seleccione su opcion: ").strip()

        if opactor == "1":
            listar_peliculas_por_genero()
        elif opactor == "2":
            listar_peliculas_por_actor()
        elif opactor == "3":
            buscar_pelicula_por_id()
        elif opactor == "4":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opcion no valida")

# Llamada a la función principal del programa
mostrar_menu()
