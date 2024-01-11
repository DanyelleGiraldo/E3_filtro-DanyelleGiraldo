import json


def cargar_base_datosgeneros():
    try:
        with open("Generos.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"genero": []}
    return data

def Creargenero():
    idgenero = input("Ingrese el ID del genero: ")
    nombregenero = input("Ingrese el nombre del genero: ")

    genero = {
        "id": idgenero,
        "nombre": nombregenero
    }

    data = cargar_base_datosgeneros()
    data["genero"].append([genero])  

    with open("Generos.json", "w") as file:
        json.dump(data, file, indent=2)

    print("Género inscrito exitosamente.")

def listargeneros():
    data = cargar_base_datosgeneros()

    if data["genero"]:
        print("Listado de géneros registrados:")
        for lista_genero in data["genero"]:
            for genero in lista_genero:
                if isinstance(genero, dict):  
                    print(f"ID: {genero['id']}, Nombre: {genero['nombre']}")
    else:
        print("No hay géneros registrados.")


