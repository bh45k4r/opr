#/bin/env bash

if [ "$1" == "dev" ]
then
    echo "sourcing virtualenv..."
    source venv/bin/activate

    echo "installing dependencies..."
    pip3 install --quiet --requirement requirements.txt

    echo "starting flask..."
    FLASK_APP=app.py FLASK_ENV=development flask run
else
    echo "starting docker image..."
    docker run --publish 8080:8080 bh45k4r/opr
fi

