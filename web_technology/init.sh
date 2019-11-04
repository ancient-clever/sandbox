sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo /etc/init.d/mysql start

sudo pip install pymysql
sudo pip3 install pymysql

cd /home/box/web/ask
sudo bash /home/box/web/mysql.sh
sudo python3 manage.py makemigrations qa
sudo python3 manage.py migrate qa

sudo ln -s /home/box/web/etc/gunicorn-wsgi.conf /etc/gunicorn.d/test
sudo gunicorn ask.wsgi:application --bind 0.0.0.0:8000
