FROM python:3.14

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

# Use exec form (JSON array) and correct uvicorn spelling.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]