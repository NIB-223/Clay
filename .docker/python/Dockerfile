FROM python:3.8-buster

VOLUME /app
WORKDIR /app

COPY requirements.txt requirements.txt
COPY .docker/python/uwsgi.ini /uwsgi.ini
COPY .docker/python/entrypoint.sh /entrypoint.sh

# Necessary for files edited on windows
RUN sed -i 's/\r$//' /entrypoint.sh

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 49152 49152

CMD sh /entrypoint.sh
