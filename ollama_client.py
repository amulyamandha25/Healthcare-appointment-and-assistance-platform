import ollama


MODEL_NAME = "llama3.2"


SYSTEM_PROMPT = """
You are an AI healthcare assistance chatbot.

Your role is to provide general healthcare information
in simple and easy-to-understand language.

Rules:

- Do not diagnose diseases.
- Do not prescribe medicines.
- Do not provide medication dosages.
- Do not tell users to stop prescribed medication.
- Do not replace a qualified doctor.
- Encourage users to consult a healthcare professional.
- If the user describes a possible emergency, tell them
  to seek immediate medical attention.
- Keep responses clear and concise.

You can also help users understand which medical
specialization may be appropriate for their concern.
"""


def ask_ai(question):

    try:

        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response["message"]["content"]

    except Exception as error:

        return (
            "❌ Unable to connect to Ollama.\n\n"
            f"Error: {error}\n\n"
            "Please make sure Ollama is running and "
            "the llama3.2 model is installed."
        )
