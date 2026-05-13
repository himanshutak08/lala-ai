from tools.automation_tool import create_automation
from ollama_client import ask_ollama

def run_agent(prompt: str):

    lower = prompt.lower()

    if "create automation" in lower:
        return create_automation(prompt)

    return ask_ollama(prompt)