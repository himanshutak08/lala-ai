# Lala AI - Home Assistant Ollama Add-on

Claude-style local AI assistant for Home Assistant using Ollama.

## Features

- Local Ollama integration
- Natural language automation creation
- YAML generation
- Home Assistant automation reload
- Safe file editing
- Local-first privacy

## Example

```txt
Create automation:
Turn off all lights at 11 PM
```

## Run

```bash
docker build -t lala-ai .
docker run -p 8099:8099 lala-ai
```