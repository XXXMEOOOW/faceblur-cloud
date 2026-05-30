FROM python:3.11-slim

WORKDIR /app

COPY worker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY worker ./worker
COPY shared ./shared

WORKDIR /app/worker

CMD ["python", "worker.py"]