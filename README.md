# Cinewild

All your favorites movies in one app !

# Installation :

- Clone project
- python installation : Python 3.7.0

| Package | Version |
|---------|---------|
| Django  |   2.1   | 
| Pillow  |   5.2.0 | 

- Create ```media``` and ```static``` directories in your file system
- Create environnement variables : 
  - MEDIA=```media directory```
  - STATIC=```static directory```
  - DEBUG=True
  - SECRET_KEY='''your_secret_key'''

# Running the project

In the directory of manage.py, enter the commands :

    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py collectstatic
    $ python manage.py runserver

After this last command, the project is running !
