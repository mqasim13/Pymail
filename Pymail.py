 #Python Command Line Email App

import smtplib
import getpass

#Ask user for his email and password
sender = raw_input("Please put in your email")
password = raw_input("Email password please")
#Ask user where to send email 
recepient = raw_input("Please put person email")
#Ask user for message 
message = raw_input("Insert message")

try:
	session = smtplib.SMTP("smtp.gmail.com:587")v
	session = smtplib.SMTP("mailgate.sfu.ca:587")
#session = smtplib.SMTP()
	print("sucess")
#session.connect("smtp.gmail.com", 587)
	session.ehlo()
	print("hi1")
	session.starttls
	print("hi")
	session.ehlo()
	print("work")
	#having issues with this specific command
	session.login(sender, password)
	print ("sucess2")
	session.sendmail(sender, [recepient], message)
	print("success3")
	session.quit
	print("message sent :)")
except smtplib.SMTPException:
	print("message not send :(")








"""import yagmail 

#Ask user for email address
sender = raw_input("What is your email")
pswd = raw_input("What is your email password")
yagmail.register('sender', 'pswd')
yag = yagmail.SMTP(sender)
#Ask user for email address they want to send to 
recepient = raw_input("What email address do you want to send to?")
subject = raw_input("What is the subject of your email?")
#Ask user what to put in email
msg = raw_input("Insert Email body")

#sending email
yag.send(recepient, subject, content = msg)
"""

