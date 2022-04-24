# build stage

FROM node:lts-alpine as build-stage

# Make the 'app' folder the current working directory
WORKDIR /app

# Copy both package.json and package-lock.json if available
COPY package*.json ./

# Install the project dependencies
RUN npm install

# Copy the project files and folders to the current working directory (i.e 'app' directory)
COPY . .

# Build the app for production
RUN npm run build



# production stage

FROM nginx:stable-alpine as production-stage

# Copy the configuration file for nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy the build files from the previous stage to nginx
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Expose port 80 (port for http requests)
EXPOSE 80

# Start the nginx server
CMD ["nginx", "-g", "daemon off;"]