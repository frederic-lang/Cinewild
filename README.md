# Cinewild

All your favorites movies in one app !

# Installation :

- Clone project
- python installation : Python 3.7.0

| Package | Version |
|---------|---------|
| Django  |   2.1   | 
| Pillow  |   5.2.0 | 

- Create ```media``` directory in your file system
- Set MEDIA_ROOT in cinewild/settings.py to your ```media`` directory

# Running the project

In the directory manage.py, enter the commands :

    $ python manage.py createsuperuser
    $ python manage.py migrate
    $ python manage.py runserver

After this last command, the project is running !
