#!/usr/bin/with-contenv bashio

echo "Starting Ollama..."

ollama serve &

sleep 10

echo "Pulling model..."

ollama pull qwen2.5:3b

echo "Starting terminal..."

ttyd -W -p 7681 bash