echo off
cd %CD%
cls
pipenv run python manage.py runserver 127.0.0.1:80
pause