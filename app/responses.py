INTENTS = {
    "greeting": {
        "patterns": [
            "hello",
            "hi",
            "hey"
        ],
        "response": "Hello! How can I help you today!"
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

    "help": {
        "patterns": [
            "help",
            "commands"
        ],
        "response":
            "Available commands:\n"
            "- hello\n"
            "- hi\n"
            "- hey\n"
            "- who are you\n"
            "- how are you\n"
            "- help\n"
            "- exit"
    }
}