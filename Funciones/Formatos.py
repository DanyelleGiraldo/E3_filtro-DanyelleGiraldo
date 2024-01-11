import json

def cargar_base_datosformatos():
    try:
        with open("Formatos.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"formato": []}
    return data

def crearformato():
    idformato = input("Ingrese el ID del formato: ")
    nombreformato = input("Ingrese el nombre del formato: ")
    precioformato = input("Ingrese el precio del formato: ")

    formato = {
        "id": idformato,
        "nombre": nombreformato,
        "precio": precioformato
    }

    data = cargar_base_datos()
    data["formato"].append(formato)

    with open("Formatos.json", "w") as file:
        json.dump(data, file, indent=2)

    print("Formato inscrito exitosamente.")

def listaformatos():
    data = cargar_base_datos()

    if data["formato"]:
        print("Listado de formatos registrados:")
        for formato in data["formato"]:
            print(f"ID: {formato.get('id')}, Nombre: {formato.get('nombre')}, Precio: {formato.get('precio')}")
    else:
        print("No hay formatos registrados.")


