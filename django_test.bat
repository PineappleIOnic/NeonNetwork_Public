echo off
cd %CD%
cls
start http://127.0.0.1/
pipenv run python manage.py runserver 127.0.0.1:80
pause