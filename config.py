import os


TOKEN = '893093320:AAE6y55UJQtIpM4sbhgQBUlrrKpTOTP9Xbg'
APP_NAME = 'quiet-tundra-76001.herokuapp.com'
HOST = "0.0.0.0"
PORT = int(os.environ.get('PORT', 5000))
DATABASE_URL = os.environ['DATABASE_URL']

STATS_MAP = {
    0: 'Утро, Команда 1',
    1: 'Утро, Команда 2',
    2: 'Утро, Команда 3',
    3: 'Вечер, Команда 1',
    4: 'Вечер, Команда 2',
    5: 'Вечер, Команда 3',
}

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1d9syrNBKeFy6Ppmn0xn-AUfagNBX3ydmGvpjr4gth2k'
RANGE_NAME = 'Статистика!A2:E4'

CREDENTIALS_FILE = 'Update Bot-a0f23bbb96e3.json'
