lista_compra = {}

def lista():
    print("Lista de la compra: ")
    for articulo, cantidad in lista_compra.items():
        print(f"-{articulo}: {cantidad}")

def añadir_item():
    x = input("Ingrese el nombre de su item: ")
    y = input("La cantidad: ")
    lista_compra[x] = y

def eliminar_item():
    x = input("Ingrese el nombre de su item")
    del lista_compra[x]

def eleccion(respuesta):
    match respuesta:
        case 'añadir':
            return añadir_item()
        case 'eliminar':
            return eliminar_item()
        case 'mostrar':
            return lista()

while True:
    print("¿Qué desea hacer?")
    respuesta = input('Desea "añadir", "elimina" o "mostrar"')
    if respuesta.lower() == 'salir':
        break
    else:
        eleccion(respuesta)