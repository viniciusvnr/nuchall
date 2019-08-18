FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt ./requirements.txt
COPY /app_config ./app_config
COPY /controllers ./controllers
COPY /schemas ./schemas
COPY /services ./services
COPY run.py .
COPY api_v1.py .

EXPOSE 5000

RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "run.py" ]