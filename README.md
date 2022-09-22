# systemTest

Technologies used
Django: The web framework for perfectionists with deadlines (Django builds better web apps with less code).
DRF: A powerful and flexible toolkit for building Web APIs

Installation
If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python here.

After doing this, confirm that you have installed virtualenv globally as well. If not, run this:

    $ pip install virtualenv
Then, Git clone this repo to your PC

    $ git clone https://github.com/kunalksng/systemTest.git
    
    Dependencies
Cd into your the cloned repo as such:
    $ cd django-rest-api
Create and fire up your virtual environment:
    $ virtualenv  venv -p python3
    $ source venv/bin/activate
Install the dependencies needed to run the app:
    $ pip install -r requirements.txt
Make those migrations work
    $ python manage.py makemigrations
    $ python manage.py migrate
Run It
Fire up the server using this one simple command:

    $ python manage.py runserver
