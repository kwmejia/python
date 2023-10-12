from functions.functions import actualizar_item,mostrar_inventario,eliminar_producto,agregar
import pandas as pd
import os
import time

def exportar_excel(inventario):
    if not inventario:
        print("El inventario está vacío, no hay nada que exportar.")
        return

    df = pd.DataFrame(inventario)
    nombre_archivo = input("Ingrese el nombre del archivo de Excel para exportar (sin extensión): ")
    try:
        df.to_excel(f"{nombre_archivo}.xlsx", index=False)
        print(f"Inventario exportado con éxito a {nombre_archivo}.xlsx.")
    except Exception as e:
        print(f"Ocurrió un error al exportar el archivo: {e}")



def main():
    invetario = []
   
    while True:
        input("Presione Enter para continuar...")
        print("\n---- Sistema de Inventario ------")
        print("1. Mostrar inventario")
        print("2. Añadir  inventario")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Exportar a Excel")
        print("6. Salir")

        opcion = input("Elija una opcion: ")

        if(opcion == "1"):
            mostrar_inventario(invetario)
        elif(opcion == "2"):
            agregar(invetario)
        elif(opcion == "3"):
            actualizar_item(invetario)
        elif(opcion == "4"):
            eliminar_producto(invetario)
        elif(opcion == "5"):
            exportar_excel(invetario)
        elif(opcion == "6"):
            break

main()
