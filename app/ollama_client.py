import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = '''
You are Lala AI.
You help create Home Assistant automations.
'''

def ask_ollama(prompt, model="qwen2.5-coder:3b"):

    payload = {
        "model": model,
        "prompt": SYSTEM_PROMPT + "\n" + prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    return response.json()["response"]