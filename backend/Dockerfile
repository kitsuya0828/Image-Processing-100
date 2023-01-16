FROM python:3.9-slim

WORKDIR /server

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]