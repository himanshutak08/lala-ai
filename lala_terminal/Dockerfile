ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache \
    bash \
    ttyd \
    python3 \
    py3-pip \
    py3-requests \
    py3-rich

COPY app /app
COPY run.sh /run.sh

RUN chmod +x /run.sh
RUN chmod +x /app/lala

CMD ["/run.sh"]