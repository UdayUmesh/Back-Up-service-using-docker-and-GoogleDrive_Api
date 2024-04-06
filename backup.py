# import os
# import time
# import datetime
# import json
# import pickle
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from googleapiclient.discovery import build
# from googleapiclient.http import MediaFileUpload

# # Path to the directory you want to back up
# BACKUP_DIR = 'C:\\Users\\Uday.U\\Desktop\\6thsem\\CC\\BackUpSerivce\\BackupFiles'

# # Path to the Google Drive API credentials JSON file
# CREDENTIALS_FILE = './credentials.json'

# def backup_to_gdrive():
#     creds = None

#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = Credentials.from_authorized_user_info(info=json.load(token))

#     if not creds or not creds.valid:
#         flow = InstalledAppFlow.from_client_secrets_file(
#             CREDENTIALS_FILE, ['https://www.googleapis.com/auth/drive.file'])
#         creds = flow.run_local_server(port=0)

#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)

#     drive_service = build('drive', 'v3', credentials=creds)

#     for filename in os.listdir(BACKUP_DIR):
#         file_path = os.path.join(BACKUP_DIR, filename)
#         file_metadata = {'name': filename}
#         media = MediaFileUpload(file_path, resumable=True)
#         drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
#         print(f'Backed up {filename} to Google Drive')

#     print(f'Backup completed at {datetime.datetime.now()}')

# if __name__ == '__main__':
#     while True:
#         backup_to_gdrive()
#         time.sleep(3600)  # Wait for 1 hour (3600 seconds) before the next backup

# import os
# import time
# import datetime
# import json
# import pickle
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from googleapiclient.discovery import build
# from googleapiclient.http import MediaFileUpload

# # Path to the directory you want to back up
# BACKUP_DIR = 'C:\\Users\\Uday.U\\Desktop\\6thsem\\CC\\BackUpSerivce\\BackupFiles'

# # Path to the Google Drive API credentials JSON file
# CREDENTIALS_FILE = '/app/credentials.json'

# # Path to the token.pickle file
# TOKEN_FILE = os.path.join('/app', 'token.pickle')

# def backup_to_gdrive():
#     creds = None
#     if os.path.exists(TOKEN_FILE):
#         try:
#             with open(TOKEN_FILE, 'rb') as token:
#                 creds = Credentials.from_authorized_user_info(info=json.load(token))
#         except (UnicodeDecodeError, FileNotFoundError):
#             # Handle the case where the token.pickle file is not found or has expired credentials
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 CREDENTIALS_FILE, ['https://www.googleapis.com/auth/drive.file'], 
#                 redirect_uri='urn:ietf:wg:oauth:2.0:oob')
#             creds = flow.run_console()
#             with open(TOKEN_FILE, 'wb') as token:
#                 pickle.dump(creds, token)
#     else:
#         # Handle the case where the token.pickle file is not found
#         flow = InstalledAppFlow.from_client_secrets_file(
#             CREDENTIALS_FILE, ['https://www.googleapis.com/auth/drive.file'], 
#             redirect_uri='urn:ietf:wg:oauth:2.0:oob')
#         creds = flow.run_console()
#         with open(TOKEN_FILE, 'wb') as token:
#             pickle.dump(creds, token)

#     drive_service = build('drive', 'v3', credentials=creds)
#     for filename in os.listdir(BACKUP_DIR):
#         file_path = os.path.join(BACKUP_DIR, filename)
#         file_metadata = {'name': filename}
#         media = MediaFileUpload(file_path, resumable=True)
#         drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
#         print(f'Backed up {filename} to Google Drive')
#     print(f'Backup completed at {datetime.datetime.now()}')

# if __name__ == '__main__':
#     while True:
#         backup_to_gdrive()
#         time.sleep(3600)  # Wait for 1 hour (3600 seconds) before the next backup

import os
import time
import datetime
import json
import pickle
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Path to the directory you want to back up
BACKUP_DIR = '/app/BackupFiles'

# Path to the Google Drive API credentials JSON file
CREDENTIALS_FILE = '/app/credentials.json'

# Path to the token.pickle file
TOKEN_FILE = os.path.join('/app', 'token.pickle')

def backup_to_gdrive():
    creds = None
    if os.path.exists(TOKEN_FILE):
        try:
            with open(TOKEN_FILE, 'rb') as token:
                creds = Credentials.from_authorized_user_info(info=json.load(token))
        except UnicodeDecodeError:
            # Handle the case where the token.pickle file has encoding issues
            with open(TOKEN_FILE, 'rb') as token:
                creds = pickle.load(token)
        except FileNotFoundError:
            # Handle the case where the token.pickle file is not found
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, ['https://www.googleapis.com/auth/drive.file'], 
                redirect_uri='urn:ietf:wg:oauth:2.0:oob')
            creds = flow.run_local_server(port=0)
            with open(TOKEN_FILE, 'wb') as token:
                pickle.dump(creds, token)
    else:
        # Handle the case where the token.pickle file is not found
        flow = InstalledAppFlow.from_client_secrets_file(
            CREDENTIALS_FILE, ['https://www.googleapis.com/auth/drive.file'], 
            redirect_uri='urn:ietf:wg:oauth:2.0:oob')
        creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    drive_service = build('drive', 'v3', credentials=creds)
    for filename in os.listdir(BACKUP_DIR):
        file_path = os.path.join(BACKUP_DIR, filename)
        file_metadata = {'name': filename}
        media = MediaFileUpload(file_path, resumable=True)
        drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f'Backed up {filename} to Google Drive')
    print(f'Backup completed at {datetime.datetime.now()}')

if __name__ == '__main__':
    while True:
        backup_to_gdrive()
        time.sleep(60)  # Wait for 1 hour (3600 seconds) before the next backup