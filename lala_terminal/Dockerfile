FROM ghcr.io/home-assistant/aarch64-base:latest

RUN apk add --no-cache \
    bash \
    curl \
    python3 \
    py3-pip \
    py3-requests \
    py3-rich \
    ttyd

RUN curl -fsSL https://ollama.com/install.sh | sh

COPY app /app
COPY run.sh /run.sh

RUN chmod +x /run.sh
RUN chmod +x /app/lala

CMD ["/run.sh"]