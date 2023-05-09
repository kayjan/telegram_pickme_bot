FROM python:3.8-slim

USER root
COPY . /telegram_pickme_bot
WORKDIR /telegram_pickme_bot

RUN pip install pip --upgrade \
    && pip install -U -r requirements.txt
RUN ls -lh
ENTRYPOINT python -m main
# ENTRYPOINT uvicorn src.app_init:app --host=0.0.0.0 --port=80
