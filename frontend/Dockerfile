FROM node:18-bullseye-slim
WORKDIR /frontend
# COPY package.json ./
# COPY yarn.lock ./
COPY . ./
RUN yarn install

CMD ["yarn", "dev"]