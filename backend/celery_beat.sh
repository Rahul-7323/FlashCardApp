venv=".env"

if [ -d $venv ]; then
    echo "Activating virtual environment"
    echo "Starting the application"
    . ${venv}/bin/activate
    export ENV="DEVELOPMENT"
    celery -A main.celery beat --max-interval 1 -l info
    echo "deactivating virtual environment"
    deactivate
else
    echo "No virtual environment present, run setup..."
fi;