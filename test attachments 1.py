# -*- coding: iso-8859-1 -*-
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
 
msg = MIMEMultipart()
msg['Subject'] = 'Email From Python jajaja'
msg['From'] = 'dairon@ceac.cu'
msg['Reply-to'] = 'otroemail@dominio'
msg['To'] = 'rms@gnu.org'
 
# That is what u see if dont have an email reader:
msg.preamble = 'Multipart massage.\n'
 
# This is the textual part:
part = MIMEText("Hello im sending an email from a python program")
msg.attach(part)
 
# This is the binary part(The Attachment):
part = MIMEApplication(open("file.pdf","rb").read())
part.add_header('Content-Disposition', 'attachment', filename="file.pdf")
msg.attach(part)
 
# Create an instance in SMTP server
smtp = SMTP("smtp.domain.cu")
# Start the server:
smtp.ehlo()
smtp.login("yo@example.com", "mipassword")
 
# Send the email
smtp.sendmail(msg['From'], msg['To'], msg.as_string())