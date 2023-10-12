

def mostrar_invetario(inventory):
    if not inventory:
        print("El inventario esta vacio")
    else:
        print("\nInventario actual:")
        for index, product in enumerate(inventory):
            print(f"Índice: {index}, Nombre: {product['name']}, Cantidad: {product['quantity']}, Precio: {product['price']}")

def add_product(inventory):
    name = input("Ingrese el nombre del producto: ")
    quantity = int(input("Ingrese la cantidad del producto: "))
    price = float(input("Ingrese el precio del producto: "))
    inventory.append({'name': name, 'quantity': quantity, 'price': price})
    print("Producto añadido exitosamente.")




def main():
    inventory = []

    while True:
        print("\n---- Sistema de Inventario ------")
        print("1. Mostrar inventario")
        print("2. Añadir  inventario")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        choice = input("Elija una opcion: ")

        if choice == '1':
            mostrar_invetario(inventory)
        if choice == '2':
            add_product(inventory)

main()