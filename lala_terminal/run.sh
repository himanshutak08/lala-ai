#!/usr/bin/with-contenv bashio

echo "=================================="
echo "Starting Lala Terminal..."
echo "=================================="

echo "Starting Ollama..."
ollama serve &

sleep 10

echo "Pulling AI model..."
ollama pull qwen2.5:3b

echo "Starting web terminal..."

ttyd -W -p 7681 bash