import openai

MODEL = 'gpt-3.5-turbo'
MAX_RESPONSE_TOKEN = 100
TEMPERATURE = 0.8

def get_completion(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_RESPONSE_TOKEN
    )
    return response.choices[0].message.content