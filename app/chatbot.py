from app.logger import logger
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

    The chatbot continuously:
    1. Accepts user input.
    2. Validates the input using guardrails.
    3. Normalizes the input.
    4. Processes the intent.
    5. Displays the corresponding response.
    6. Exits gracefully when an exit command is received.
    """

    print("=" * 40)
    print(f" {BOT_NAME} ")
    print("=" * 40)
    print(WELCOME_MESSAGE)

    logger.info("Chatbot started.")

    while True:
        user_input = input("\nYou: ")

        # Guardrail Layer
        is_valid, message = validate_input(user_input)

        if not is_valid:
            logger.warning(f"Validation failed: {message}")
            print(f"Bot: {message}")
            continue

        # Input Normalization
        clean_input = normalize_input(user_input)

        # Graceful Exit
        if clean_input in EXIT_COMMANDS:
            logger.info("Chatbot terminated.")
            print("Bot: Goodbye! Have a great day.")
            break

        # Intent Processing
        response = process_intent(clean_input)

        print(f"Bot: {response}")