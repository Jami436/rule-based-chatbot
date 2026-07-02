from app.responses import INTENTS
from app.constants import FALLBACK_RESPONSE


def process_intent(clean_input: str) -> str:
    """
    Returns the chatbot response for a given normalized input.
    """

    return INTENTS.get(clean_input, FALLBACK_RESPONSE)