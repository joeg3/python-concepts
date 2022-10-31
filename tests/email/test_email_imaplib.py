import imaplib, email
from datetime import date

import pytest

from src.email.email_reader_imaplib import EmailReader

 # Tests using Python's built in imaplib email library
@pytest.mark.skip(reason='Keep tests fast')
def test_imaplib_read_inbox(config):
    email_api = EmailReader( config['email-host'], config['username'], config['password'], 'INBOX')
    emails = email_api.get_all_emails()
    count = 0
    for email in emails:
        count+=1
        print_new_email(email)
    print('Number of emails in inbox: ', count)

@pytest.mark.skip(reason='Keep tests fast')
def test_imaplib_get_todays_emails(config):
    email_api = EmailReader( config['email-host'], config['username'], config['password'], 'INBOX')
    emails = email_api.get_todays_emails()
    count = 0
    for email in emails:
        count+=1
        print_new_email(email)
    print('Number of emails from today', count)

def print_email(id, date, sender, subject, message):
    print("-------------------------------------------------------")
    print('Id: ', id)
    print('Date: ', date)
    print('Sender: ', sender)
    print('Subject: ', subject)
    print('Message: ', message)

def print_new_email(email):
    print("-------------------------------------------------------")
    print("Id: " + email["id"])
    print("Date: " + email["date"])
    print("From: " + email["from"])
    print("Subject: " + email["subject"])
    print("Message: " + email["body"])
