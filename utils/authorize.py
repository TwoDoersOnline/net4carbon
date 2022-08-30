from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from os.path import exists


class Auth:
    cred = 'sheets.googleapis.com-python.json'
    DATA = ['client_secret.json', 'credentials.json', 'token.json']
    SCOPE = ['https://www.googleapis.com/auth/spreadsheets']

    if exists('token.json'):
        cred = Credentials.from_authorized_user_file('token.json', SCOPE)
    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config('credentials.json', SCOPE)
            cred = flow.run_local_server(port=0)
        with open('token.json', 'w') as f:
            f.write(cred.to_json())
            f.close()
    try:
        service = build('testing', 'v4', Credentials='credentials.json')
    except HttpError as err:
        print(err)

class Sensor()