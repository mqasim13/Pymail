 #Python Command Line Email App

import smtplib
import getpass

# Note: user must visit "https://www.google.com/settings/security/lesssecureapps" first and allow less secure apps for this application to work
#Ask user for his email and password
sender = raw_input("Please enter your gmail email address: ")
password = getpass.getpass("Please enter your email password: ")
#Ask user where to send email 
recepient = raw_input("Please put in the targets email: ")
#Ask user for email subject
subject	= raw_input("Please put in email subject: ")
#Ask user for message 
message = raw_input("Input the desired message: ")
signConfirm = raw_input("Y to confirm signature, N to omit ")
if(signConfirm == "y") or (signConfirm == "Y"):
	signature = raw_input("Please add signature ")
else:
	signature = ""

#create a proper header + subject for the email + signature
header = "To: " + recepient + "\n" + "From: " + sender + "\n" + "Subject: " + subject + "\n"
footer = "\n" + signature
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
