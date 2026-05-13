FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl

RUN pip install fastapi uvicorn requests pyyaml

COPY app /app

WORKDIR /app

CMD ["python", "main.py"]