FROM node:lts-alpine

RUN npm install -g http-server

COPY package*.json ./

RUN npm install

COPY . .

#RUN npm run build
#EXPOSE 8080
#CMD [ "http-server", "dist" ]
#CMD ["npm", "run", "serve"]