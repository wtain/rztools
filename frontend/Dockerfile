# syntax=docker/dockerfile:1

# https://mherman.org/blog/dockerizing-a-react-app/

FROM node:18.7.0-alpine

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent
RUN npm install react-scripts@5.0.1 -g --silent

# add app
COPY . ./

# start app
ENV CHOKIDAR_USEPOLLING "true"
CMD ["npm", "start"]