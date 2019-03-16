import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from settings import MAIL_SMTP, MAIL_IMAP


class EmailHandler():
    def __init__(self, login, password):
        self.login = login
        self.password = password
    
    def send_message(self, recipients, subject, message_text):
        message = MIMEMultipart()
        message['From'] = self.login
        message['To'] = ', '.join(recipients)
        message['Subject'] = subject
        message.attach(MIMEText(message_text))

        smtp_connection = smtplib.SMTP("smtp.mail.ru")
        # identify ourselves to smtp gmail client
        smtp_connection.ehlo()
        # secure our email with tls encryption
        smtp_connection.starttls()
        # re-identify ourselves as an encrypted connection
        smtp_connection.ehlo()

        smtp_connection.login(self.login, self.password)
        smtp_connection.sendmail(self.login, message['To'], message.as_string())
        smtp_connection.quit()
        print('Message sent!')

    def recieve_message(self, header = None):
        mail = imaplib.IMAP4_SSL(MAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("Inbox")
        criterion = f'(HEADER Subject {header})' if header else "ALL"
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        print(data)
        print(result + '\n\n')
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        mail.logout()
        return email_message


if __name__ == '__main__':
    subject = 'Test subject'
    recipients = ['alexey.sherchenkov@yandex.ru', 'mr.paralon@gmail.com', 'Alsherchenkov@mail.ru']
    message_text = "Test message"
    my_email = EmailHandler('Alsherchenkov@mail.ru', 'K)^CtG^q7')
    my_email.send_message(recipients, subject, message_text)
    all_emails = my_email.recieve_message()
    print(all_emails)
    print('done')



