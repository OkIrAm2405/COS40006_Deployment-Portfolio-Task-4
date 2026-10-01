FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN adduser --disabled-password --gecos "" appuser && \
    mkdir -p /data && \
    chown -R appuser:appuser /app /data

COPY .dockerignore .
COPY processor.py .

USER appuser

VOLUME ["/data"]

ENTRYPOINT ["python", "processor.py"]
CMD ["--name", "Default-Batch", "--size", "5"]