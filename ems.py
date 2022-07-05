from datetime import datetime
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders


def send_mail(send_from, send_to, subject, text, files, server, port, username='', password='', isTls=True):
    tgl = datetime.today().strftime("%d-%m-%y")
    server = "smtp.gmail.com"
    password = "eaauyyswikrxswzn"
    username = "thomihidayat1@gmail.com"
    port = 
    filename = tgl + ".xlsx"
    msg = MIMEMultipart()
    msg['From'] = "thomihidayat1@gmail.com"
    msg['To'] = "hidayatthomi@gmail.com"
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "Ems daily report"
    msg.attach(MIMEText(text))

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(filename, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename={}'.format(filename))
    msg.attach(part)

    # context = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
    # SSL connection only working on Python 3+
    smtp = smtplib.SMTP(server, port)
    if isTls:
        smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()
