# Archivo: todo_list.py

# Inicializa una lista vacía para almacenar las tareas
tasks = []

def show_menu():
    print("\n--- Menu ---")
    print("1. Añadir tarea")
    print("2. Mostrar tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

def add_task():
    task = input("Introduce la nueva tarea: ")
    tasks.append(task)
    print(f'Tarea "{task}" añadida.')

def show_tasks():
    if len(tasks) == 0:
        print("No hay tareas en la lista.")
    else:
        print("\n--- Tareas Pendientes ---")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def delete_task():
    show_tasks()
    try:
        index = int(input("\nIntroduce el número de la tarea que deseas eliminar: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Índice inválido.")
        else:
            deleted_task = tasks.pop(index)
            print(f'Tarea "{deleted_task}" eliminada.')
    except ValueError:
        print("Por favor, introduce un número válido.")

while True:
    show_menu()
    choice = input("Selecciona una opción: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Hasta luego!")
        break
    else:
        print("Opción no válida, por favor intenta de nuevo.")
