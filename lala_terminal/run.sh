#!/usr/bin/with-contenv bashio

ollama serve &

sleep 5

ollama pull qwen2.5:3b

ttyd -W -p 7681 bash