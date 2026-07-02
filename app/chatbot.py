from app.normalizer import normalize_input
from app.processor import process_intent
from app.constants import EXIT_COMMANDS, WELCOME_MESSAGE


def start_chatbot():
    print("=" * 40)
    print(" Rule-Based AI Chatbot ")
    print("=" * 40)
    print(WELCOME_MESSAGE)

    while True:
        user_input = input("\nYou: ")

        clean_input = normalize_input(user_input)

        if clean_input in EXIT_COMMANDS:
            print("Bot: Goodbye! Have a great day.")
            break

        response = process_intent(clean_input)
        print(f"Bot: {response}")