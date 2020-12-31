import smtplib, glob
from decouple import config
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login(config('EMAIL'), config('PASSWORD'))

server.ehlo()
msg = MIMEMultipart()
msg['From'] = config('EMAIL')
msg['To'] = config('TO')
msg['Subject'] = "Python wallpaper"

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = glob.glob('*.jpg')[0]

attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()

server.sendmail(config("TO"), config('EMAIL'), text)