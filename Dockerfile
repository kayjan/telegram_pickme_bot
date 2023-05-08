FROM python:3.8-slim
ARG port

USER root
COPY . /telegram_pickme_bot
WORKDIR /telegram_pickme_bot

ENV PORT=$port

RUN pip install pip --upgrade \
    && pip install -U -r requirements.txt
RUN ls -lh
CMD uvicorn src.app_init:app
