FROM python:3.10
WORKDIR .
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python", "Telegram_bot\main.py"]
