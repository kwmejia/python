
def mostrar_inventario(invetario):
    if not invetario:
        print("El invetario esta vacio")
    else:
        print("\n Lista de items")
        for index, item in  enumerate(invetario):
            print(index,". -",item['name'])


def agregar(invetario):
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese el nombre del producto: "))
    precio = float(input("Ingrese el precio del producto; "))

    invetario.append({'name': nombre,'cantidad': cantidad, 'precio': precio})
    print("Producto añadido exitosamente.")

def actualizar_item(inventario):
    mostrar_inventario(inventario)

    if not inventario:
        return
    index = int(input("Ingrese el índice del producto que desea actualizar: "))
    if index < 0 or index >= len(inventario):
        print("Índice no válido.")
        return
    
    print(f"Actualizando {inventario[index]['name']}...")

    nuevo_nombre = input("Ingrese el nuevo nombre del producto (enter para mantener el mismo): ")
    nuevo_cantidad = input("Ingrese la nueva cantidad del producto (enter para mantener el mismo): ")
    nuevo_precio = input("Ingrese el nuevo precio del producto (enter para mantener el mismo): ")
    if nuevo_nombre:
        inventario[index]['name'] = nuevo_nombre
    if nuevo_cantidad:
        inventario[index]['cantidad'] = int(nuevo_cantidad)
    if nuevo_precio:
        inventario[index]['precio'] = float(nuevo_precio)

    print("Producto actualizado exitosamente.")

def eliminar_producto(inventario):
    mostrar_inventario(inventario)
    
    if not inventario:
        return
    
    try:
        index = int(input("Ingrese el índice del producto que desea eliminar: "))
        if index < 0 or index >= len(inventario):
            print("Índice no válido.")
            return

        print(f"Eliminando {inventario[index]['name']}...")
        inventario.pop(index)
        print("Producto eliminado exitosamente.")
    except ValueError:
        print("Entrada no válida, asegúrese de ingresar un número para el índice.")
