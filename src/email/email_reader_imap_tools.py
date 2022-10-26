import imaplib, email
#from email_config import gmail_pass, user, host
from email.header import decode_header



class EmailReader:
    """An example of a Python email reader using the imap_tools library"""

    def __init__(self, server, username, password):
        """Login to email account"""
        self.server = server
        self.username = username
        self.password = password
        self.imap = imaplib.IMAP4_SSL(server)
        print('username: ', self.username)
        print('password: ', self.password)
        self.imap.login(self.username, self.password)

    def connect(self):
        #imap = imaplib.IMAP4_SSL(self.server)
        print('username: ', self.username)
        print('password: ', self.password)
        self.imap.login(self.username, self.password)

    def get_num_messages(self, folder):
        status, messages = self.imap.select(folder)
        print('Status: ', status)
        count = int(messages[0])
        return count

    def print_messages(self, folder):
        self.imap.select(folder)
        typ, data = self.imap.search(None, 'ALL')
        for num in data[0].split():
            typ, data = self.imap.fetch(num, '(RFC822)')
            print('Message %s\n%s\n' % (num, data[0][1]))

    def iterate_through_messages(self, folder):
        status, messages = self.imap.select(folder)
        count = int(messages[0])
        for i in messages:
            # RFC822 protocol
            res, msg = self.imap.fetch(str(i), "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])

                # Store the senders email
                sender = msg["From"]

                # Store subject of the email
                subject = msg["Subject"]

                print("-"*50)  # To divide the messages
                print("From    : ", sender)
                print("Subject : ", subject)

