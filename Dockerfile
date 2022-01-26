FROM python:3.7-alpine

WORKDIR /app

ADD requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ADD . .

CMD ["python3", "-u","SubjectDatabase.py"]
