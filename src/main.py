import sys
import os

MAX_CELL_LENGTH = 10000
 
# Tells python to look in the projec dir
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import json, os
from config import SCOPES, SPREADSHEET_ID, SHEET_RANGE, STATE_FILE
from gmail_service import get_gmail_service
from sheets_service import get_sheets_service, append_row
from email_parser import parse_email

def load_state():
    if os.path.exists(STATE_FILE):
        return set(json.load(open(STATE_FILE)))
    return set()

def save_state(ids):
    json.dump(list(ids), open(STATE_FILE, "w"))

def main():
    gmail = get_gmail_service(SCOPES)
    sheets = get_sheets_service(gmail._http.credentials)

    processed_ids = load_state()

    results = gmail.users().messages().list(
        userId="me", labelIds=["INBOX", "UNREAD"]
    ).execute()

    for msg in results.get("messages", []):
        if msg["id"] in processed_ids:
            continue

        email = parse_email(gmail, msg["id"])

        content = email["content"][:MAX_CELL_LENGTH]

        append_row(
            sheets,
            SPREADSHEET_ID,
            SHEET_RANGE,
            [email["from"], email["subject"], email["date"], content] #Large emails are safely truncated
        )

        gmail.users().messages().modify(
            userId="me",
            id=msg["id"],
            body={"removeLabelIds": ["UNREAD"]}
        ).execute()

        processed_ids.add(msg["id"])

    save_state(processed_ids)

if __name__ == "__main__":
    main()
