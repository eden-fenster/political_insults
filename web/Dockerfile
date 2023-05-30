# syntax=docker/dockerfile:1

FROM python:3.10.6

WORKDIR /political_insults_web_directory

ENV FLASK_APP=web/app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY web/requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install inetutils-ping
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000


COPY web/*.py /political_insults_web_directory/web/
COPY web/templates/*.html /political_insults_web_directory/web/templates/
COPY web/static/styles/*.css /political_insults_web_directory/web/static/styles/
COPY web/static/scripts/*.js /political_insults_web_directory/web/static/scripts/

CMD ["flask", "run"]