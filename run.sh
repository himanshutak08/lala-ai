#!/bin/bash

ollama serve &

sleep 10

ollama pull qwen2.5-coder:3b

python3 /app/main.py