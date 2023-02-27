from datetime import date
import pytest
from src.email.email_reader_imaplib import EmailReader

from imap_tools import MailBox, AND

# Tests using the PyPi third-party imap_tools email library
@pytest.mark.skip(reason='Keep tests fast')
def test_imap_tools_read_inbox(config):
    with MailBox(config['email-host']).login(config['username'], config['password'], initial_folder='INBOX') as mailbox:
        count = 0
        for msg in mailbox.fetch():
            count+=1
            print_email(msg.uid, msg.date, msg.from_, msg.subject, msg.text)
        print('Number of emails in inbox: ', count)

@pytest.mark.skip(reason='Keep tests fast')
def test_imap_tools_get_todays_emails(config):
    with MailBox(config['email-host']).login(config['username'], config['password'], initial_folder='INBOX') as mailbox:
        count = 0
        for msg in mailbox.fetch(AND(date=date.today())):
            count+=1
            print_email(msg.uid, msg.date, msg.from_, msg.subject, msg.text)
        print('Number of emails from today', count)

@pytest.mark.skip(reason='Keep tests fast')
def test_imap_tools_delete_ibm_email(config):
    with MailBox(config['email-host']).login(config['username'], config['password'], initial_folder='INBOX') as mailbox:
        for msg in mailbox.fetch(AND(date=date.today())):
            print_email(msg.uid, msg.date, msg.from_, msg.subject, msg.text)
            if 'ibm' in msg.text:
                print('!!!!!!!!!Need to delete', msg.uid )
                mailbox.delete(msg.uid)

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
    print("Subject: " + email["subject"])
    print("From: " + email["from"])
    print(email["body"])
