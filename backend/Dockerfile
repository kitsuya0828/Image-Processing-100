FROM python:3.9-slim

WORKDIR /backend

COPY requirements-docker.txt ./
RUN pip install --no-cache-dir --upgrade -r ./requirements-docker.txt

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]