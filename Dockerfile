FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

copy . .


EXPOSE 8000

CMD ["python", "website/manage.py", "runserver", "0.0.0.0:8000"]