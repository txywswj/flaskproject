ps ax|grep gunicorn|grep -v grep|cut -d ' ' -f1|xargs kill
tail logs/app.log
