FROM python:3.10-slim

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get update &&\
    apt-get install -y wget gnupg curl
WORKDIR /chromium-driver
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - &&\
    wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb &&\
    apt-get install -y ./google-chrome-stable_current_amd64.deb &&\
    rm google-chrome-stable_current_amd64.deb

RUN pip install --upgrade pip &&\
    pip install poetry &&\
    poetry config virtualenvs.create false
