FROM python:3.7-alpine as base

FROM base as builder

RUN pip install -U pip

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local
COPY src/ /app

EXPOSE 5000

WORKDIR /app

CMD ["flask", "run", "--host=0.0.0.0"]
