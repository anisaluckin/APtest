FROM python:3.7-slim AS builder
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

FROM python:3.7-slim

# Copy over only virtualenv
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN apt-get update && apt-get install -y postgresql gdal-bin libpq-dev

COPY ./start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

ADD . /code/

WORKDIR /code

ENTRYPOINT ["/start"]