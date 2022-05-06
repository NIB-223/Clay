FROM node:latest

VOLUME /app
WORKDIR /app

COPY .docker/node/app/package.json /app/package.json

COPY .docker/node/entrypoint.sh /entrypoint.sh
# Necessary for files edited on windows
RUN sed -i 's/\r$//' /entrypoint.sh

EXPOSE 4040 4040

CMD sh /entrypoint.sh
