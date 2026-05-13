import yaml
from pathlib import Path
from ollama_client import ask_ollama

AUTOMATION_DIR = "/config/packages/ai_generated"

SYSTEM = '''
Generate valid Home Assistant YAML only.
'''

def create_automation(prompt):

    yaml_text = ask_ollama(SYSTEM + "\n" + prompt)

    Path(AUTOMATION_DIR).mkdir(parents=True, exist_ok=True)

    file_path = f"{AUTOMATION_DIR}/generated.yaml"

    parsed = yaml.safe_load(yaml_text)

    with open(file_path, "w") as f:
        yaml.dump(parsed, f)

    return f"Automation created at {file_path}"