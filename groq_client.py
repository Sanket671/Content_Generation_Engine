import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_groq(system_prompt, user_prompt):
    try:
        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],

            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"Warning: GROQ request failed ({e}). Using fallback text.")
        return "<p>This is fallback content because the language model API is unavailable right now.</p>"