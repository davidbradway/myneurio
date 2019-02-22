FROM python:3-alpine
RUN pip install -U pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . /app
WORKDIR /app
CMD ["flask", "run", "--host=0.0.0.0"]
