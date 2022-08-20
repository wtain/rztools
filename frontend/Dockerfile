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
# Downgrade to 4.0.3 as suggested here:
# https://github.com/facebook/create-react-app/issues/11879
# in order to make watch mode work again
RUN npm install react-scripts@4.0.3 -g --silent
RUN npm install axios
RUN npm install @types/axios
# RUN npm i axios-react

# add app
COPY . ./

# start app
ENV WDS_SOCKET_PORT=3000
# In the end this one helped
ENV WATCHPACK_POLLING=true
ENV CHOKIDAR_USEPOLLING "true"
CMD ["npm", "start"]