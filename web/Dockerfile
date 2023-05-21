# syntax=docker/dockerfile:1

FROM python:3.10.6

WORKDIR /political_insults_web

ENV FLASK_APP=web/app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY web/requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install inetutils-ping
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000


COPY web/*.py /political_insults_web/web/
COPY web/templates/*.html /political_insults_web/web/templates/
COPY web/static/*.css /political_insults_web/web/static/

CMD ["flask", "run"]