import os
import re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ask_chatbot(resume_text, question):
    if not resume_text:
        return "Please upload resume first."

    if not question.strip():
        return "Ask a valid question."

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a professional resume evaluator. "
                        "Give clear, simple, professional answers. "
                        "Do not use bullet points, stars, bold text, or any symbols. "
                        "Respond in plain clean paragraphs only."
                    )
                },
                {
                    "role": "user",
                    "content": f"Resume:\n{resume_text}\n\nQuestion:\n{question}"
                }
            ],
            temperature=0.2
        )

        reply = completion.choices[0].message.content.strip()
        reply = re.sub(r"[*#•\-]", "", reply)
        reply = re.sub(r"\s+", " ", reply)
        return reply

    except Exception as e:
        return f"Chat error: {str(e)}"
