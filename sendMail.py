import smtplib

sender = 'dd@mail.hyman.store'
receivers = ['daiybh@qq.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('mail.hyman.store')
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except Exception as e :
   print("Error: unable to send email")
   print(e)