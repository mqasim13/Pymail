import smtplib 
import getpass
import sys
from mimetypes import guess_type
from email.mime.base import MIMEBase
from email.encoders import encode_base64
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


sender = raw_input("Please enter your gmail email address: ")
#TODO use validate_email to verify email address
password = getpass.getpass("Please enter your email password: ")
#Ask user where to send email 
recepient = raw_input("Please put in the targets email: ")
#Ask user for email subject
subject	= raw_input("Please put in email subject: ")
#Ask user for message 
message = raw_input("Input the desired message: ")
#attachments
#attachments = [sys.argv[0]]
#Asking user if they want signature
signConfirm = raw_input("Y to confirm signature, N to omit ")
#If Y for signature asks for signature else leaves signature empty
if(signConfirm == "y") or (signConfirm == "Y"):
	signature = raw_input("Please add signature ")
else:
	signature = ""

attachConfirm = raw_input("Y to confirm attachment, N to omit ")
#If Y for signature asks for attachment else leaves signature empty
if (attachConfirm == "y") or (attachConfirm == "Y"):
	filename = raw_input("Please add full filename: ")
mimetype, encoding = guess_type(filename)
mimetype = mimetype.split('/', 1)
fp = open(filename, 'rb')
attachment = MIMEBase(mimetype[0], mimetype[1])
attachment.set_payload(fp.read())
fp.close()
encode_base64(attachment)
attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filename))
self.email.attach(attachment)


#create a proper header + subject for the email + signature
header = "To: " + recepient + "\n" + "From: " + sender + "\n" + "Subject: " + subject + "\n"
footer = "\n" + signature + "\n" + "Sent from Pymail"
message = header + message + "\n" + footer


try:
	session = smtplib.SMTP("smtp.gmail.com", 587)
	session.ehlo()
	session.starttls()
	session.ehlo()
	session.login(sender, password)
	session.sendmail(sender, [recepient], message)
	session.quit
	print("message sent :)")
except Exception, e:
	print("message not sent :(. Exception: " +  str(e))
