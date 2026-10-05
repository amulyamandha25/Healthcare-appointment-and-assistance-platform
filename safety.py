EMERGENCY_KEYWORDS = [

    "chest pain",
    "difficulty breathing",
    "cannot breathe",
    "can't breathe",
    "severe bleeding",
    "unconscious",
    "loss of consciousness",
    "stroke",
    "face drooping",
    "sudden weakness",
    "overdose",
    "suicidal"

]


def check_emergency(text):

    text = text.lower()

    for keyword in EMERGENCY_KEYWORDS:

        if keyword in text:
            return True

    return False
