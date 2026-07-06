INTENTS = {
    "greeting": {
        "patterns": [
            "hello",
            "hi",
            "hey"
        ],
        "response": "Hello! How can I help you today?"
    },

    "identity": {
        "patterns": [
            "who are you",
            "what are you"
        ],
        "response": "I am a deterministic rule-based chatbot."
    },

    "status": {
        "patterns": [
            "how are you",
            "how are you doing"
        ],
        "response": "I'm functioning normally. Thanks for asking!"
    },

    "capabilities": {
        "patterns": [
            "what can you do",
            "what do you do",
            "what are your capabilities"
        ],
        "response": (
            "I can greet users, answer predefined questions, "
            "validate input using guardrails, and exit gracefully."
        )
    },

    "help": {
        "patterns": [
            "help",
            "commands"
        ],
        "response": (
            "Available commands:\n"
            "- hello / hi / hey\n"
            "- who are you / what are you\n"
            "- how are you / how are you doing\n"
            "- what can you do\n"
            "- help / commands\n"
            "- exit / quit / bye"
        )
    }
}