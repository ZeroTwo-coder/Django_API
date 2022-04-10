Import Library and create env
    
    python -m venv env
    source env/bin/activate
    pip install -r req.txt

Start Project:

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
