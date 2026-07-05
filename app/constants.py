"""
Application-wide constants for the Rule-Based AI Chatbot.
"""

# Chatbot Configuration

BOT_NAME = "Rule-Based AI Chatbot"

WELCOME_MESSAGE = (
    "Welcome! Type 'exit', 'quit', or 'bye' to quit."
)

# Exit Commands

EXIT_COMMANDS = {
    "exit",
    "quit",
    "bye"
}

# Responses

FALLBACK_RESPONSE = (
    "Sorry, I don't understand that command."
)

# Guardrail Configuration

MAX_INPUT_LENGTH = 100

EMPTY_INPUT_RESPONSE = (
    "Input cannot be empty."
)

LONG_INPUT_RESPONSE = (
    f"Input exceeds the maximum allowed length of {MAX_INPUT_LENGTH} characters."
)