FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt ./requirements.txt
COPY /app_config ./app_config
COPY /controllers ./controllers
COPY /schemas ./schemas
COPY /services ./services
COPY /tests ./tests
COPY setup.py .
COPY run.py .

EXPOSE 5000
RUN chmod +x ./setup.py
RUN chmod +x ./tests/test_rules.py

RUN pip3 install --no-cache-dir -r requirements.txt
RUN python3 setup.py install

RUN python3 ./tests/test_rules.py

ENTRYPOINT [ "python3" ]

CMD [ "run.py" ]