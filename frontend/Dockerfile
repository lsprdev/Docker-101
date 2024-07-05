FROM node:16    
WORKDIR /app
# install vite globally
RUN npm install -g vite
# copy all filtes
COPY . .    
# install all deps
RUN npm i

# vite default port
EXPOSE 5173    
CMD ["npm", "run", "dev"]