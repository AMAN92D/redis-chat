FROM python:3.7.1-stretch

WORKDIR /usr/local/src

COPY ./flask_web_server/requirements.txt requirements.txt

RUN apt-get update
RUN apt-get install --no-install-recommends -y gcc make
RUN pip3 install --no-cache-dir -r requirements.txt