FROM python:3.10-slim

WORKDIR /app

RUN pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic

COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]