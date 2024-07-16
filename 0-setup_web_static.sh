#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

if ! command -v nginx &>/dev/null; then
	sudo apt-get -y update
	sudo apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/{releases,shared}
sudo mkdir -p /data/web_static/releases/test/

cat << EOT | sudo tee /data/web_static/releases/test/index.html
<html>
    <head>
    </head>
    <body>
		<h2>Hello World!</h2>
    	<p>This is a test to show that Nginx is well configured and working</p>
    </body>
</html>
EOT

if test -e /data/web_static/current; then
	sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo cat << EOT | sudo tee new_conf_file
        location /hbnb_static {
            alias /data/web_static/current;
            index index.html index.html index.nginx-debian.html;
	}
EOT
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bkp
sudo sed -i '56r new_conf_file' /etc/nginx/sites-available/default
sudo rm new_conf_file

if [ "$(pgrep -c nginx)" -le 0 ]; then
        sudo service nginx start
else
        sudo service nginx restart
fi
