
# File location: todo_list_excel.py
import pandas as pd

def display_tasks(tasks):
    if not tasks:
        print("La lista de tareas está vacía.")
    else:
        print("\nLista de tareas:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Ingrese la tarea que desea agregar: ")
    tasks.append(task)
    print(f"Se ha agregado la tarea: {task}")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
        if index < 0:
            print("Número inválido.")
            return
        removed_task = tasks.pop(index)
        print(f"Se ha eliminado la tarea: {removed_task}")
    except (IndexError, ValueError):
        print("Número inválido.")

def export_to_excel(tasks):
    df = pd.DataFrame({'Tareas': tasks})
    try:
        df.to_excel("lista_de_tareas.xlsx", index=False)
        print("Lista de tareas exportada a 'lista_de_tareas.xlsx'")
    except Exception as e:
        print(f"Ocurrió un error al exportar: {e}")

def main():
    tasks = []
    while True:
        print("\n--- Lista de Tareas ---")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Exportar a Excel")
        print("5. Salir")
        
        choice = input("Elige una opción: ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            export_to_excel(tasks)
        elif choice == '5':
            print("Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
