cd %CD%
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate --run-syncdb
pipenv run python manage.py migrate
pause