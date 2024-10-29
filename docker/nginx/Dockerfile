# Use the official Nginx image
FROM nginx:latest

# Update the package list and upgrade packages
RUN apt update && apt upgrade -y

# Remove the default Nginx configuration file
RUN rm -f /etc/nginx/conf.d/default.conf

# Copy your custom Nginx configuration file to the appropriate location
COPY nginx.conf /etc/nginx/conf.d/nginx.conf