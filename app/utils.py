import random

easy_words = ["hello", "world", "code", "python", "flask", "text"]
medium_words = ["accuracy", "keyboard", "developer", "monkeytype", "result"]
hard_words = ["synchronization", "asynchronous", "functionality", "architecture", "visualization"]

def generate_text(level="easy"):
    word_pool = {
        "easy": easy_words,
        "medium": medium_words,
        "hard": hard_words
    }.get(level, easy_words)
    return " ".join(random.choices(word_pool, k=40))
