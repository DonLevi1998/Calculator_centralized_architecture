FROM python:3.11-slim

WORKDIR /app

COPY Calculator_centralized_architecture.py .

CMD ["python", "Calculator_centralized_architecture.py"]
