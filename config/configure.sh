#!/bin/bash
# Update and install necessary packages
sudo apt-get update -y
sudo apt-get install -y nginx python3-pip
# Create NGINX configuration
sudo bash -c 'cat << 'EOT' > /etc/nginx/sites-available/project.conf
server {
listen 80;
server_name _;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
EOT'
# Enable the new NGINX configuration
sudo ln -s /etc/nginx/sites-available/project.conf /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
# Restart the service
sudo service nginx restart
# Download docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
# Clone the GitHub repository
git clone https://github.com/venessafoong/WebScraper.git
cd WebScraper
# Build Docker image and run container
sudo docker build -t api .
nohup docker run -p 8000:8000 api