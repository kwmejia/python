# Archivo: rock_paper_scissors.py
import random

def show_menu():
    print("\n--- Menú ---")
    print("1. Jugar")
    print("2. Salir")

def play_game():
    # Lista de opciones
    options = ['piedra', 'papel', 'tijera']
    
    while True:
        # Elección del jugador
        print("\nOpciones: piedra, papel, tijera")
        player_choice = input("¿Cuál es tu elección? ").lower()

        if player_choice not in options:
            print("Elección inválida. Inténtalo de nuevo.")
            continue
        
        # Elección del ordenador
        computer_choice = random.choice(options)
        print(f"La computadora eligió {computer_choice}.")

        # Determinar el ganador
        if player_choice == computer_choice:
            print("Es un empate.")
        elif (player_choice == 'piedra' and computer_choice == 'tijera') or \
             (player_choice == 'papel' and computer_choice == 'piedra') or \
             (player_choice == 'tijera' and computer_choice == 'papel'):
            print("¡Ganaste!")
        else:
            print("Perdiste.")

        # Preguntar si desea jugar otra ronda
        another_round = input("\n¿Quieres jugar otra ronda? (s/n): ").lower()
        if another_round != 's':
            break

while True:
    show_menu()
    choice = input("Elige una opción: ")
    
    if choice == '1':
        play_game()
    elif choice == '2':
        print("Hasta luego!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
