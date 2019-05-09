# Python-projects
1. projects use library turtle
2. server with python use virtual enviroment `virtualenv` and  microframework for Python `flask`


## Use
1. Install python3 and tkinter for SO
2. On terminal `$ python3 [name_project.py]`
## Use server python on virtual enviroment
1. install `virtualenv` `$ sudo pip install virtualenv`
2. Init module `venv` `$ virtualenv venv`
3. install freeze `$ sudo pip install freeze`
4. install python-dotenv `$ sudo pip install python-dotenv`
4. init enviroment `$ source venv/bin/activate`
5. install flask `(venv)$ pip install flask`

## create application

main.py

```python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

```
requirements.txt

```python
Flask==1.0.2

```

.flaskenv

```python
FLASK_APP=main.py
FLASK_ENV=development

```

## run

`(env)$ flask run`

## Skills applied
1. python
2. micro framework flask

Skills applied: https://platzi.com/clases/python/

Any question? contact me silgajuandiego@gmail.com