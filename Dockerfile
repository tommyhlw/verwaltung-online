# syntax=docker/dockerfile:1
FROM alpine:latest

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apk add python3
RUN apk add py3-pip
RUN apk add openssl
RUN apk add py3-cryptography

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./
COPY wsgi.py ./
COPY verwaltungonline verwaltungonline
EXPOSE 5000
#ENTRYPOINT [ "sh" ]
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
