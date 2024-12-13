FROM ubuntu:latest
LABEL authors="andre"
# Dockerfile
FROM python:3.9
RUN apt-get update && apt-get install -y \
libpq-dev \
&& pip install --upgrade pip
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]