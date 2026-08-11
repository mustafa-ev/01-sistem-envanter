FROM python:3.10-slim

WORKDIR /app

COPY sistem_bilgi.py .

RUN pip install psutil

CMD ["python", "sistem_bilgi.py"]