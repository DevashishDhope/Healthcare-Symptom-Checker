DISCLAIMER_TEXT = (
    "This is for educational purposes only. "
    "Consult a doctor for medical advice. "
    "This system does not provide medical diagnoses or treatment instructions."
)

def validate_symptom_input(text: str) -> bool:
    # Basic validation to ensure input isn't empty or too short
    if not text or len(text.strip()) < 3:
        return False
    return True
