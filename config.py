import os


TOKEN = '588048354:AAFgl8K6V4JSoc9Cs3v4PlgNT2zfNHg0XcU'
APP_NAME = 'voyage-livre-89482.herokuapp.com'
HOST = "0.0.0.0"
PORT = int(os.environ.get('PORT', 5000))
DATABASE_URL = os.environ['DATABASE_URL']
