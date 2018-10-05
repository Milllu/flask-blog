import os.path

from flask import Flask 

from apps.tools import creat_folder

app = Flask(__name__)
app.debug = True

APPS_DIR = os.path.dirname(__file__)
UPLOADS_FOLDER = os.path.join(APPS_DIR, 'static')


app.config['SECRET_KEY'] = 'are you ok!'
app.config['DATABASE'] = os.path.join(APPS_DIR, 'data.db')
app.config['UPLOADS_FOLDER'] = os.path.join(UPLOADS_FOLDER, 'uploads')

creat_folder(app.config['UPLOADS_FOLDER'])


import apps.views
