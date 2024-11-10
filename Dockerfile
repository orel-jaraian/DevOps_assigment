# Start from the Ubuntu base image
FROM ubuntu:latest

# Install Nginx
RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean

# Copy the custom Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose the two ports for the servers
EXPOSE 8080 8081

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
