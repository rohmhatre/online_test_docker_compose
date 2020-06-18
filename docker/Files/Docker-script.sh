#!/bin/bash 
chown -R apache /Sites/online_test
chown -R apache /Sites/online_test/yaksh
chown -R nobody /Sites/online_test/yaksh_data
chmod -R 664 /Sites/online_test
chmod -R +X /Sites
cd /Sites/online_test
/etc/init.d/celeryd start
python3 manage.py makemigrations
python3 manage.py makemigrations notifications_plugin
python3 manage.py migrate
python3 manage.py collectstatic --noinput
sed -i "s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = \[\'\*'\]/g" /Sites/online_test/online_test/settings.py
sed -i "s/'redis\:\/\/localhost'/'redis\:\/\/yaksh\-redis'/g" /Sites/online_test/online_test/settings.py
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python3 manage.py shell
/usr/sbin/httpd -D FOREGROUND
