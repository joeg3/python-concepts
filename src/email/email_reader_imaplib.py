import imaplib, email
from datetime import date
#from email_config import gmail_pass, user, host
from email.header import decode_header



class EmailReader:
    """An example of a Python email reader using the built in imaplib library"""

    def __init__(self, server, username, password, folder):
        """Login to email account"""
        self.server = server
        self.username = username
        self.password = password
        self.session = imaplib.IMAP4_SSL(server)
        self.session.login(self.username, self.password)
        self.session.select(folder, readonly = False)

    def get_all_emails(self):
        message, data = self.session.search(None, 'ALL')
        emails =  data[0].split()
        return self.__process_emails(emails)

    def get_todays_emails(self):
        today = date.today().strftime('%d-%b-%Y')
        message, data = self.session.search(None, 'ON', '"%s"' % today)
        emails =  data[0].split()
        return self.__process_emails(emails)

    def __process_emails(self, emails):
        """ For each email, need to fetch its data """
        processed_emails = [ ]

        if len(emails) == 0:
            return processed_emails

        first = int(emails[0])
        last = int(emails[-1])

        #for i in emails:
        for i in range(last,first-1, -1):
            email = self.__fetch_email(i)
            processed_emails.append(email)

        return processed_emails

    def __fetch_email(self, email_message):
        emailObject = {}

        message = self.session.fetch(str(email_message), "(RFC822)")

        for response in message:
            responseDetails = response[0]
            
            if isinstance(responseDetails, tuple):
                messageObject = email.message_from_string(str(responseDetails[1],'utf-8'))
                # print('messageObject.keys', messageObject.keys()) # See all available keys of message object
                emailObject["id"] = str(email_message) #messageObject['Message-Id']
                emailObject["date"] = messageObject['date']
                emailObject["subject"] = messageObject['subject']
                emailObject["from"] = messageObject['from']

                if messageObject.is_multipart():

                    for part in messageObject.walk():
                        contentType = part.get_content_type()
                        disposition = str(part.get("Content-Disposition"))

                        try:
                            emailBody = part.get_payload(decode=True).decode()

                            if contentType == "text/plain" and "attachment" not in disposition:
                                emailObject["body"] = emailBody

                        except Exception as e:
                            pass
                        
                else:
                    contentType = messageObject.get_content_type()
                    emailBody = messageObject.get_payload(decode=True).decode()

                    if contentType == "text/plain":
                        emailObject["body"] = emailBody

        return emailObject

######################

    def get_num_messages(self, folder):
        status, messages = self.session.select(folder)
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

