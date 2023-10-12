# Archivo: quiz_game.py
import random

def show_menu():
    print("\n--- Menú ---")
    print("1. Jugar")
    print("2. Salir")

def play_game():
    # Lista de preguntas y respuestas
    questions = [
        {
            'question': '¿Cuál es la capital de Francia?',
            'options': ['Madrid', 'Berlín', 'París', 'Roma'],
            'answer': 'París'
        },
        {
            'question': '¿Qué planeta es conocido como el Planeta Rojo?',
            'options': ['Tierra', 'Marte', 'Júpiter', 'Venus'],
            'answer': 'Marte'
        },
        {
            'question': '¿Cuántos lados tiene un triángulo?',
            'options': ['1', '3', '4', '5'],
            'answer': '3'
        },
    ]
    
    # Mezclar la lista de preguntas
    random.shuffle(questions)
    
    # Iniciar contador de respuestas correctas
    score = 0
    
    for i, question_data in enumerate(questions):
        print(f"\nPregunta {i + 1}: {question_data['question']}")
        
        # Mostrar opciones
        for j, option in enumerate(question_data['options']):
            print(f"{j + 1}. {option}")
        
        # Obtener respuesta del jugador
        try:
            player_answer = int(input("\nSelecciona tu respuesta (1-4): "))
            if player_answer < 1 or player_answer > 4:
                print("Opción inválida.")
                continue
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue
        
        # Verificar respuesta
        if question_data['options'][player_answer - 1] == question_data['answer']:
            print("Correcto!")
            score += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: {question_data['answer']}")
    
    print(f"\nJuego terminado. Tu puntuación es {score}.")

while True:
    show_menu()
    choice = input("Selecciona una opción: ")
    
    if choice == '1':
        play_game()
    elif choice == '2':
        print("Hasta luego!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
