FROM python:3

EXPOSE 5000

WORKDIR /app

COPY /app_config ./app_config
COPY /controllers ./controllers
COPY /schemas ./schemas
COPY /services ./services
COPY run.py .
COPY api_v1.py .
COPY requirements.txt .


RUN pip install -r requirements.txt

CMD [ "python", "run.py" ]