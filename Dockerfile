FROM python:3.10
RUN pip3 install -r requirements.txt
WORKDIR /usr/src/app
COPY /usr/src/app .
ENTRYPOINT ["python"]
CMD ["main.py"]
