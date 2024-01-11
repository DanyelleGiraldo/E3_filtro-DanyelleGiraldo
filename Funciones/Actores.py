import json


def guardar_base_de_datos_actores(data):
    with open("Actores.json", "w") as file:
        json.dump(data, file, indent=2)


def cargar_base_datosactores():
    try:
        with open("Actores.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"actor": []}
    return data

def crearactor():
    idactor = input("Ingrese el ID del Actor: ")
    nombreactor = input("Ingrese el nombre del Actor: ")
    papelactor = input("Ingrese el papel del actor: ")

    actores= []
    actor = {
        "id": idactor,
        "nombre": nombreactor,
        "papel": papelactor
    }
    actores.append(actor)
    data = cargar_base_datosactores()
    data["actor"].append(actores)

    with open("Actores.json", "w") as file:
        json.dump(data, file, indent=2)

    print("Actor inscrito exitosamente.")

def listaractores():
    data = cargar_base_datosactores()

    if data["actor"]:
        print("Listado de Actores registrados:")
        for lista_actores in data["actor"]:
            for actor in lista_actores:
                print(f"ID: {actor.get('id')}, Nombre: {actor.get('nombre')}, Papel: {actor.get('papel')}")
    else:
        print("No hay actores registrados.")


