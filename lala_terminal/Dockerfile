FROM ghcr.io/home-assistant/aarch64-base:latest

RUN apk add --no-cache \
    bash \
    curl \
    git \
    python3 \
    py3-pip \
    py3-requests \
    py3-rich \
    ttyd \
    zstd \
    ca-certificates

RUN curl -fsSL https://ollama.com/install.sh | sh

COPY app /app
COPY rootfs /

RUN chmod +x /app/lala
RUN chmod +x /etc/services.d/lala/run