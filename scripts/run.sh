# remove content of front (previous data) and copy from tmp folder to /frontend to reflect updates
rm -rf /frontend/build/* && cp -r /frontend_tmp/build/* /frontend/build
python manage.py migrate
python manage.py collectstatic --no-input
gunicorn -w 4 -b 0.0.0.0:8000 project_settings.wsgi:application



