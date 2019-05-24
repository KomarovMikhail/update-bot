import os


TOKEN = '893093320:AAE6y55UJQtIpM4sbhgQBUlrrKpTOTP9Xbg'
APP_NAME = 'quiet-tundra-76001.herokuapp.com'
HOST = "0.0.0.0"
PORT = int(os.environ.get('PORT', 5000))
DATABASE_URL = os.environ['DATABASE_URL']
