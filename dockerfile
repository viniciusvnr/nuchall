FROM python:3.7-slim


ADD requirements.txt /requirements.txt
ADD setup.py /setup.py

RUN set -ex \
    && python3.7 -m venv /venv \
    && /venv/bin/pip install -U pip \
    && /venv/bin/pip install --no-cache-dir -r /requirements.txt

WORKDIR /app
COPY . /app

RUN set -ex \
    && /venv/bin/python3.7 -m unittest tests

EXPOSE 5000


CMD ["/venv/bin/python", "run.py"]