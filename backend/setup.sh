venv=".env"
requirements="requirements.txt"

if [ -d $venv ]; then
    echo "Virtual environment present"
else
    echo "No virtual environment present, creating one..."
    pip install virtualenv
    python3 -m venv $venv
    echo "Created the virtual environment"
fi;

if ! [ -f $requirements ]; then
    echo "$requirements not present"
    echo "Creating a dummy $requirements"
    echo "flask" > $requirements
fi;

echo "Activating virtual environment"
. ${venv}/bin/activate
echo "Installing packages"
pip install -r $requirements
echo "Installed all the packages"
pip freeze > $requirements
echo "Deactivating the virtual environment"
deactivate
echo "Setup complete : )"
