from app.constants import (
    MAX_INPUT_LENGTH,
    EMPTY_INPUT_RESPONSE,
    LONG_INPUT_RESPONSE,
)


def validate_input(user_input: str) -> tuple[bool, str | None]:
    """
    Validate user input before it reaches the chatbot engine.

    Args:
        user_input: Raw input provided by the user.

    Returns:
        A tuple containing:
        - True and None if the input is valid.
        - False and an error message if the input is invalid.
    """

    if not user_input.strip():
        return False, EMPTY_INPUT_RESPONSE

    if len(user_input) > MAX_INPUT_LENGTH:
        return False, LONG_INPUT_RESPONSE

    return True, None