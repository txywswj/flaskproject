cd /home/lzp/Desktop/flaskproject
/home/lzp/Desktop/flaskproject/env/bin/gunicorn -w4 -D wsgi
ps aux|grep gunicorn|grep tigereye|grep -v grep


