FROM python:3.10.12-alpine

WORKDIR /app

COPY trilium_client ./trilium_client
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY cogs cogs
COPY utils utils
COPY *.py .

CMD ["python3", "bot.py"]
