import smtplib
import time
import schedule
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from datetime import datetime
from email import encoders


def kirim_ems():
    fromaddr = "thomihidayat1@gmail.com"
    toaddr = ["hidayatthomi@gmail.com", "0001indahratna@gmail.com"]
    tgl = datetime.today().strftime("%d-%m-%y")
    # membuat MIMEMultipart
    print("membuat pesan....")
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = ", ".join(toaddr)
    msg['Subject'] = "EMS Daily Report " + tgl
    body = "Please find the attached file here.."
    msg.attach(MIMEText(body, 'plain'))
    print("pesan jadi ...! melampirkan file excel")

    try:
        filename = tgl + ".xlsx"
        attachment = open(filename, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
        print("mengirim email....ke " + ", ".join(toaddr))
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "eaauyyswikrxswzn")
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        print("email terkirim ke " + ", ".join(toaddr))
        print("laporan EMS tanggal..." + tgl + " telah dikirim")
        print("menunngu laporan hari esok trus kirim lagi..")
        s.quit()

    except FileNotFoundError:
        print("file tidak ditemukan")
        body = "[FILE TIDAK DITEMUKAN]"
        msg.attach(MIMEText(body, 'plain'))
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "eaauyyswikrxswzn")
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()


schedule.every().day.at("00:02").do(kirim_ems)
schedule.every().day.at("00:03").do(kirim_ems)
while 1:
    schedule.run_pending()
    time.sleep(1)
