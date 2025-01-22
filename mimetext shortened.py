import smtplib
import email
from email.mime.text import MIMEText
import smtplib,email,email.encoders,email.mime.text,email.mime.base
from email.mime.multipart import MIMEMultipart

x= "kalib@netmatters.com"
msg = MIMEMultipart()

msg['Subject'] = 'Business Profitability Calculator Report'
message = 'Hello stink fart shit!'
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('smtp.gmail.com',587)
mailserver.starttls()
mailserver.ehlo()
mailserver.login('profitabilitycalculator.report@gmail.com', 'eiuw zdoa omif vtfp')

mailserver.sendmail('profitabilitycalculator.report@gmail.com',str(x),msg.as_string())