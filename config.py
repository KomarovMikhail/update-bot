import os


TOKEN = '893093320:AAE6y55UJQtIpM4sbhgQBUlrrKpTOTP9Xbg'
APP_NAME = 'quiet-tundra-76001.herokuapp.com'
HOST = "0.0.0.0"
PORT = int(os.environ.get('PORT', 5000))
DATABASE_URL = os.environ['DATABASE_URL']
CSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRdE3WC7qndjf9D4k2on2kEfQENBrn3lokCXS3eNREFzvVxwdThtP8YnBPOLifv6WHeRyXZfBoMVnIm/pub?gid=1368278468&single=true&output=csv"
