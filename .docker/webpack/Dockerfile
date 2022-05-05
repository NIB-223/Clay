FROM node:12

VOLUME /app
WORKDIR /app

COPY ./package.json /app/package.json

COPY .docker/webpack/entrypoint.sh /entrypoint.sh
# Necessary for files edited on windows
RUN sed -i 's/\r$//' /entrypoint.sh


CMD sh /entrypoint.sh
