import os, pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def get_gmail_service(scopes):
    creds = None
    if os.path.exists("token.pkl"):
        with open("token.pkl", "rb") as f:
            creds = pickle.load(f)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials/credentials.json", scopes
            )
            creds = flow.run_local_server(port=0)

        with open("token.pkl", "wb") as f:
            pickle.dump(creds, f)

    return build("gmail", "v1", credentials=creds)
