FROM python:3.10
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]
