venv=".env"

if [ -d $venv ]; then
    echo "Activating virtual environment"
    echo "Starting the application"
    . ${venv}/bin/activate
    export ENV="DEVELOPMENT"
    gunicorn main:app --worker-class gevent --bind 127.0.0.1:5000 --workers=4
    echo "deactivating virtual environment"
    deactivate
else
    echo "No virtual environment present, run setup..."
fi;