import base64

def parse_email(service, msg_id):
    msg = service.users().messages().get(
        userId="me", id=msg_id, format="full"
    ).execute()

    headers = {h["name"]: h["value"] for h in msg["payload"]["headers"]}
    payload = msg["payload"]

    body = ""
    if "parts" in payload:
        for part in payload["parts"]:
            if part["mimeType"] == "text/plain":
                body = base64.urlsafe_b64decode(
                    part["body"]["data"]
                ).decode(errors="ignore")
    else:
        body = base64.urlsafe_b64decode(
            payload["body"]["data"]
        ).decode(errors="ignore")

    return {
        "from": headers.get("From"),
        "subject": headers.get("Subject"),
        "date": headers.get("Date"),
        "content": body.strip()
    }
