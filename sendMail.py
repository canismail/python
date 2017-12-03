#!/usr/bin/python

import smtplib


#Gmail---->smtp.gmail.com(port 587)
#Outlook.com/Hotmail.com---->smtp-mail.outlook.com
#Yahoo Mail---->smtp.mail.yahoo.com
#AT&T---->smpt.mail.att.net (port 465)
#Comcast---->smtp.comcast.net
#Verizon---->smtp.verizon.net (port 465)

message = "\r\n".join((
        "From: xxx",
        "To: yyyy",
        "Subject: News",
        "",
        "",),)

def mailSender(mail_addrs):
		try:
		   server = smtplib.SMTP('smtp.gmail.com', 587)
		   sender = 'TEST-MESSAGE"'
		   server.ehlo()
		   server.starttls()
		   server.login("xxx@gmail.com", "password")
		   server.sendmail(sender, mail_addrs, message)         
		   return "Successfully sent email"
		   server.close()
		except Exception as e:
		   return "Error: E-mail don't send  "+str(e)
