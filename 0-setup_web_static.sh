#!/usr/bin/env bash
# Bash script that sets up web servers for the deployment of web_static

# Install Nginx if it not already installed
if [ ! -x /usr/sbin/nginx ]; then
    apt-get -y update
    apt-get -y install nginx
    ufw allow 'Nginx HTTP'
fi
# Create the folder /data/ if it doesn’t already exist
if [ ! -d /data/ ]; then
    mkdir /data/
fi

# Create the folder /data/web_static/ if it doesn’t already exist
if [ ! -d /data/web_static/ ]; then
    mkdir -p /data/web_static/
fi

# Create the folder /data/web_static/releases/ if it doesn’t already exist
if [ ! -d /data/web_static/releases/ ]; then
    mkdir -p /data/web_static/releases/
fi

# Create the folder /data/web_static/shared/ if it doesn’t already exist
if [ ! -d /data/web_static/shared/ ]; then
    mkdir -p /data/web_static/shared/
fi

# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
if [ ! -d /data/web_static/releases/test/ ]; then
    mkdir -p /data/web_static/releases/test/
fi

echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" >/data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/
if [ -L /data/web_static/current/ ]; then
    rm /data/web_static/current/
    ln -sf /data/web_static/releases/test/ /data/web_static/current
else
    ln -sf /data/web_static/releases/test/ /data/web_static/current
fi

chown -hR ubuntu:ubuntu /data/

sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
