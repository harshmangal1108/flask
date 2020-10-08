# Flask is micro web framework of Python,comaptible with all WSGI

### Setting Up Environement
```bash
$ mkdir url-shortner
$ cd url-shortner
## Creating Virtual Environment
$ pip3 install pipenv
$ ls
```
### Now moving on to our Virtual Enivroment's Shell
```bash
$ pipenv shell
## You are now on shell of your pipenv
## You can install packages here
$ pipenv install flask
## To start your project 
$ export FLASK_APP=filename
$ flask run
## Its running your app in production server so move to development server
$ export FLASK_ENV=development
## Everytime we start new terminal session we have to do all above things so to get rid of this rename your file to app.py
mv your_fiename.py app.py 
```
