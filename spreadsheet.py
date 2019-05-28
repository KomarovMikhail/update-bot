from config import *
from googleapiclient.discovery import build
import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from spreadsheet_handler import build_link


def get_spreadsheet():
    spreadsheet_id = build_link()
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                                   ['https://www.googleapis.com/auth/spreadsheets'])
    http_auth = credentials.authorize(httplib2.Http())
    service = build('sheets', 'v4', http=http_auth)
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=RANGE_NAME).execute()
    spreadsheet = result.get('values')
    result = (
        int(spreadsheet[0][1]),
        int(spreadsheet[1][1]),
        int(spreadsheet[2][1]),
        int(spreadsheet[0][4]),
        int(spreadsheet[1][4]),
        int(spreadsheet[2][4]),
    )
    return result
