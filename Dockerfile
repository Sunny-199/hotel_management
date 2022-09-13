<<<<<<< HEAD
#FROM python:3.10.5-alpine
#WORKDIR /Users/lovet/PycharmProjects/hotel_management_test
#
## COPY requirements.txt .
## RUN python -m pip install --upgrade pip
## RUN pip install -r requirements.txt
## COPY . .
## EXPOSE 8000
## CMD ["python", "manage.py", "runserver"]
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#RUN pip install --upgrade pip
#COPY . /Users/lovet/PycharmProjects/hotel_management_test
#
## COPY ./requirements.txt /usr/src/app
## RUN pip install -r requirements.txt
## # copy project
## COPY . /usr/src/app
#EXPOSE 8000
##COPY requirements.txt requirements.txt
#RUN pip3 install -r requirements.txt
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


=======
>>>>>>> 84f6d0a4bb50a258e33cb2862f693a996bde6e42
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

RUN apt-get update && apt-get install

COPY requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 8000

COPY . /app/

# RUN chmod 0644 /app/*

# ENTRYPOINT ["sh /app/hotel_management/migrate.sh"]

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]