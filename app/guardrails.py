from app.constants import (
    MAX_INPUT_LENGTH,
    EMPTY_INPUT_RESPONSE,
    LONG_INPUT_RESPONSE,
)


def validate_input(user_input: str):
    """
    Validate user input before it reaches the chatbot engine.

    Returns:
        tuple[bool, str | None]
    """

    if not user_input.strip():
        return False, EMPTY_INPUT_RESPONSE

    if len(user_input) > MAX_INPUT_LENGTH:
        return False, LONG_INPUT_RESPONSE

    return True, None