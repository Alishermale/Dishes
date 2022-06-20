FROM python:3.10
RUN pip3 install -r requirements.txt
WORKDIR .
COPY ..
CMD ["python", "Telegram_bot\main.py"]
