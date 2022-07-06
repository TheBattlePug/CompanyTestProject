FROM python:3.10


RUN pip install pymongo flask

COPY . /opt/app
WORKDIR /opt/app

EXPOSE 4000

ENTRYPOINT ["python3", "run.py"]

