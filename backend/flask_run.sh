venv=".env"

if [ -d $venv ]; then
    echo "Activating virtual environment"
    echo "Starting the application"
    . ${venv}/bin/activate
    export ENV="DEVELOPMENT"
    python3 main.py
    echo "deactivating virtual environment"
    deactivate
else
    echo "No virtual environment present, run setup..."
fi;