FROM node:22-alpine

ENV BACKEND_URL=http://0.0.0.0:5000

ADD . /app

WORKDIR /app

RUN npm install

ENTRYPOINT [ "npm" ]

CMD [ "start" ]