from app.responses import INTENTS
from app.constants import FALLBACK_RESPONSE
from app.logger import logger


def process_intent(clean_input: str) -> str:
    """
    Match the user's normalized input against
    predefined intent patterns.
    """

    for intent in INTENTS.values():

        if clean_input in intent["patterns"]:
            return intent["response"]

    return FALLBACK_RESPONSE