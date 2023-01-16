FROM node:16-bullseye-slim
WORKDIR /client
COPY /frontend/package.json ./
COPY /frontend/yarn.lock ./
RUN yarn install