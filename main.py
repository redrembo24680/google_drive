import gspread as gs

from oauth2client.service_account import ServiceAccountCredentials

scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name('vendor/secrets.json', scope)
client = gs.authorize(credentials=creds)
# url = 'https://docs.google.com/spreadsheets/d/1NHJa17rghZfNPM75A6_SVySDSriD4-LgUiwiriL0Sk8/edit#gid=0'
key = '1NHJa17rghZfNPM75A6_SVySDSriD4-LgUiwiriL0Sk8'


# data_url = client.open_by_url(url)
data_by_key = client.open_by_key(key)

sheet1 = data_by_key.sheet1

print(sheet1.get_all_values())


