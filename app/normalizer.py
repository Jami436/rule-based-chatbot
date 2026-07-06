def normalize_input(user_input: str) -> str:
    """
    Normalize user input by removing leading/trailing whitespace
    and converting all characters to lowercase.

    Args:
        user_input: Raw input provided by the user.

    Returns:
        A cleaned and normalized string.
    """
    return user_input.strip().lower()