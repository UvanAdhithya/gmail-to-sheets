# 📧 Gmail to Google Sheets Automation

Author: Uvan Adhithya

---

## 📖 Project Overview

This project is a **Python automation system** that reads real incoming unread emails from a Gmail inbox and logs them into a Google Sheet automatically.

Each email is added as a new row in the spreadsheet with the following details:
- Sender email address

- Email subject

- Date and time received

- Email body (plain text)

The system is designed to be safe to run multiple times, ensuring that:

- Emails are never duplicated

- Already processed emails are skipped

- Emails are marked as read after processing

---

## 🎯 Objective
- Integration with Gmail API
- Integration with Google Sheets API
- Proper use of OAuth 2.0 authentication
- Reliable automation with state persistence
- Clean, secure, and production-style code structure

## 🏗️ High-Level Architecture
```bash
Gmail Inbox (Unread Emails)
        ↓
     Gmail API
        ↓
  Email Parser (From, Subject, Date, Content)
        ↓
  Duplicate Check (Stored State)
        ↓
   Google Sheets API
        ↓
   Spreadsheet Row Added
```

## 📂 Project Structure
```bash
gmail-to-sheets/
│
├── src/
│   ├── gmail_service.py     # Gmail authentication & email fetching
│   ├── sheets_service.py   # Google Sheets interaction
│   ├── email_parser.py     # Email content extraction
│   └── main.py             # Application entry point
│
├── credentials/
│   └── credentials.json    # OAuth credentials (NOT COMMITTED)
│
├── config.py               # Configuration constants
├── requirements.txt        # Python dependencies
├── .gitignore              # Prevents secrets from being committed
└── README.md
```
---
## 🔐 Authentication (OAuth 2.0)

This project uses **OAuth 2.0 user authentication** (not service accounts).
### How it works:
1. On first run, Google opens a browser window

2. The user logs into their Gmail account

3. Permission is granted to:

4. Read Gmail inbox

5. Append rows to Google Sheets

6. Google returns a secure access token

7. The token is stored locally for reuse

**No passwords are stored**

**OAuth tokens and credentials are excluded from version control.**

---
## ⚙️ How the Script Works (Step-by-Step)

1. Authenticates with Gmail and Google Sheets
2. Fetches unread emails from the Inbox
3. Extracts:
- Sender
- Subject
- Date
- Plain-text content
4. Checks whether the email was already processed
5. Appends the email data as a new row in Google Sheets
6. Marks the email as read
7. Saves the processed email ID locally

## 🗂️ Google Sheets Output

Each processed email is added as one row:
| From                                            | Subject          | Date         | Content         |
| ----------------------------------------------- | ---------------- | ------------ | --------------- |
| [sender@example.com](mailto:sender@example.com) | Interview Update | Jan 16, 2026 | Email body text |

**Email content is safely truncated to avoid Google Sheets cell size limits.**

---

## Setup Instructions
### 1. Clone the repository
```bash
git clone https://github.com/UvanAdhithya/gmail-to-sheets.git
cd gmail-to-sheets
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Create Google Cloud credentials
- Create a Google Cloud project
- Enable:
-- Gmail API
-- Google Sheets API
- Create OAuth 2.0 Client (Desktop App)
- Download credentials.json
- Place it in:
```bash
  credentials/credentials.json
```
### 4. Configure spreadsheet
Update config.py with your Google Sheet ID.

---
## ▶️ Running the Script
```bash
python src/main.py
```

## ⚠️ Security Measures

- OAuth credentials are never committed
- Tokens are stored locally only
- .gitignore prevents accidental leaks
- Compromised credentials are rotated immediately
### What happens:
- Browser opens for OAuth (first run only)
- Unread emails are processed
- Rows are appended to Google Sheets
- Emails are marked as read

## 🧠 Challenges Faced & Solutions
**Challenge: Large email bodies**
Some emails exceeded Google Sheets’ 50,000-character cell limit.

**Solution:**
Email content is truncated before insertion to ensure reliable execution.

## 🚧 Limitations
- HTML emails may lose formatting
- Large attachments are ignored
- Gmail API rate limits apply
- Script must be run manually or scheduled
