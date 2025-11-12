FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy

# Install uv 
RUN pip install --no-cache-dir uv

WORKDIR /app

# Copy and install dependencies first to avoid reinstalling them on code changes
COPY --link requirements.txt .
RUN --mount=type=cache,target=/root/.cache/uv uv pip install --system -r requirements.txt

COPY --link counter-service.py ./counter-service.py

EXPOSE 80
CMD ["python", "counter-service.py"]
