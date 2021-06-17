#/bin/env bash

source venv/bin/activate

if [ "$1" == "dev" ]
then
    FLASK_APP=app.py FLASK_ENV=development flask run
else
    gunicorn app:app -b 127.0.0.1:8080
fi
