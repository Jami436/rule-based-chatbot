from app.normalizer import normalize_input
from app.processor import process_intent
from app.guardrails import validate_input
from app.constants import (
    EXIT_COMMANDS,
    WELCOME_MESSAGE,
    BOT_NAME,
)


def start_chatbot():
    """
    Start the chatbot interaction loop.
    """

    print("=" * 40)
    print(f" {BOT_NAME} ")
    print("=" * 40)
    print(WELCOME_MESSAGE)

    while True:

        user_input = input("\nYou: ")

        # Guardrail Layer
        is_valid, message = validate_input(user_input)

        if not is_valid:
            print(f"Bot: {message}")
            continue

        # Input Normalization
        clean_input = normalize_input(user_input)

        # Graceful Exit
        if clean_input in EXIT_COMMANDS:
            print("Bot: Goodbye! Have a great day.")
            break

        # Intent Processing
        response = process_intent(clean_input)

        print(f"Bot: {response}")