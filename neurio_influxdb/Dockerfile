FROM python:3.6-alpine
RUN pip install -U pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
CMD ["python", "neurio_influxdb.py"]4
