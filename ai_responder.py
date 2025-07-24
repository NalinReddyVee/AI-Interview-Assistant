import openai
from config import OPENAI_API_KEY

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def is_screen_question(screen_text):
    prompt = f"""
You are helping an AI monitor a technical interview.

The following appeared on the screen:
\"\"\"{screen_text}\"\"\"

Does it look like a question or prompt requiring a response? (Yes/No)
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=5
    )
    reply = response.choices[0].message.content.lower()
    return "yes" in reply


def is_question(text):
    prompt = f"""
You are helping an AI agent monitor a live job interview.

Determine if the following is a question **directed to the candidate** that requires a thoughtful answer.

Text: "{text}"

Reply with "Yes" or "No" only.
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=5,
            temperature=0.2,
        )
        reply = response.choices[0].message.content.lower()
        return "yes" in reply
    except Exception as e:
        print(f"⚠️ GPT Error (is_question): {e}")
        return False

def get_ai_response(audio_text, screen_text):
    print("screen_text:", screen_text)
    print("🤖 Generating AI response...")

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a highly experienced **senior full stack developer** currently in a technical job interview.\n"
                        "You are confident, articulate, and respond to questions with clarity and real-world experience.\n"
                        "Include examples from your background when relevant, and assume the interviewer understands the basics.\n"
                        "Respond in no more than 200 words"
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"The interviewer just said:\n\"{audio_text}\"\n\n"
                        f"The following is visible on screen (if helpful):\n\"{screen_text}\"\n\n"
                        "Based on that, how would you respond?"
                    )
                }
            ],
            max_tokens=200,
            temperature=0.3,
        )
        reply = response.choices[0].message.content.strip()
        print(f"🤖 AI Response: {reply}")
        return reply

    except Exception as e:
        print(f"⚠️ GPT Error (get_ai_response): {e}")
        return "I'm sorry, I couldn't generate a response."

def get_screen_only_response(screen_text):
    print("📺 Processing screen-only content...")
    print("screen_text:-----------", screen_text.strip())
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a senior full stack developer in a technical interview.\n"
                        "You are shown a coding problem or code snippet on screen and must respond as if asked directly.\n"
                        "\n"
                        "Your task is to:\n"
                        "- Analyze every detail carefully. Do NOT skip or overlook any part of the question, including return types, constraints, or edge cases.\n"
                        "- Use JavaScript when implementation is required.\n"
                        "- Clearly state the approach and reasoning.\n"
                        "- Include time and space complexity analysis.\n"
                        "- Use proper variable naming and clean, efficient code.\n"
                        "- Ensure the return type exactly matches what the problem expects.\n"
                        "- Consider all edge cases described or implied by the input format and constraints.\n"
                        "- If multiple possible valid outputs exist (e.g. multiple indices that work), you MUST return all of them.\n"
                        "- DO NOT stop at the first valid solution — exhaustively return all correct results as specified."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Here is what's visible on the screen:\n\n{screen_text.strip()}\n\n"
                            "What is the best possible solution or response to this problem?\n"
                            "Interpreted screen like a human.\n"
                            "Important:\n"
                            "- Follow the instructions on screen.\n"
                            "- Understand the examples if provided, and use them to solve the problem.\n"
                            "- Respect expected return types and output formats as described.\n"
                            "- If the prompt asks for multiple outputs, or multiple valid answers, provide *all* of them.\n"
                            "- Match the expected structure, edge cases, and constraints.\n"
                            "- If implementation is needed, use JavaScript.\n"
                            "- Also include time and space complexity.\n"

                    )
                }
            ],
            max_tokens=700,
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"⚠️ GPT Error (screen only): {e}")
        return "Sorry, couldn't process screen input."



def extract_clean_problem(screen_text):
    response = client.chat.completions.create(
        model="gpt-4o",  # or gpt-4-turbo
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert OCR content cleaner.\n"
                    "Your job is to extract and reconstruct the exact original problem description from screen or OCR-like content.\n"
                    "- Remove broken lines, weird formatting, smart quotes, and duplicated lines.\n"
                    "- Preserve code, math, and examples as-is.\n"
                    "- Output only the cleaned problem — no explanation.\n"
                    "- Make sure the constraints, examples, and function signature are intact and readable."
                )
            },
            {
                "role": "user",
                "content": f"Here is the raw screen text:\n\n{screen_text.strip()}\n\nPlease clean and reconstruct it accurately."
            }
        ],
        temperature=0,
        max_tokens=1000
    )
    return response.choices[0].message.content.strip()
