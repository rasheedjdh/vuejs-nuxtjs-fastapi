FROM node:12.18.4-alpine


# create destination directory
RUN mkdir -p /usr/src/nuxt-app
WORKDIR /usr/src/nuxt-app

# update and install dependency
RUN apk update && apk upgrade
RUN apk add git

# copy the app, note .dockerignore
COPY . /usr/src/nuxt-app/
RUN npm install

# expose 5000 on container
EXPOSE 3000

# start the app
CMD [ "npm", "run", "dev" ]