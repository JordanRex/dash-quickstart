FROM python:3.10.12-slim

EXPOSE 8080

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN apt-get update && apt-get install -y g++
RUN pip install --upgrade pip
RUN pip install --use-deprecated=legacy-resolver -r requirements.txt
ADD . /app/

ARG ENVIRONMENT
ENV ENVIRONMENT=$ENVIRONMENT
ARG PYTHONUNBUFFERED
ENV PYTHONUNBUFFERED=1

CMD ["python", "index.py", "prod"]
