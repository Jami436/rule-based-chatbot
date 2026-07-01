def normalize_input(user_input: str) -> str:
    """
    Normalize user input by:
    - Converting to lowercase
    - Removing leading and trailing whitespace
    """
    return user_input.strip().lower()