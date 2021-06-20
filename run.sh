#/bin/env bash

echo "sourcing virtualenv..."
source venv/bin/activate

echo "installing dependencies..."
pip3 install --quiet --requirement requirements.txt

if [ "$1" == "dev" ]
then
    echo "starting flask..."
    FLASK_APP=app.py FLASK_ENV=development flask run
else
    echo "starting gunicorn..."
    gunicorn app:app --worker-class=eventlet --bind=127.0.0.1:8080
fi

