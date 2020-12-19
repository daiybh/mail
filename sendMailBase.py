from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

import smtplib


import Emailconfig
def sendMail_Zip(z,zip_name):
    # 输入Email地址和口令:
    from_addr = Emailconfig.from_addr
    password = Emailconfig.password
    # 输入收件人地址:
    to_addr = Emailconfig.to_addr
    # 输入SMTP服务器地址:
    smtp_server = Emailconfig.smtp_server

    import time
    content="hello"+time.asctime()
    textApart = MIMEText(content)

    zipApart=MIMEApplication(z.getvalue())
    zipApart.add_header('Content-Disposition','attachment',filename=zip_name+'.zip')

    m= MIMEMultipart()

    m.attach(textApart)
    m.attach(zipApart)
    m['Subject']='proect '+zip_name

    server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
    #server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr.split(','), m.as_string())
    server.quit()


def sendMail_text(title,textContent):
    # 输入Email地址和口令:
    from_addr = Emailconfig.from_addr
    password = Emailconfig.password
    # 输入收件人地址:
    to_addr = Emailconfig.to_addr
    # 输入SMTP服务器地址:
    smtp_server = Emailconfig.smtp_server

    textApart = MIMEText(textContent)
    m= MIMEMultipart()

    m.attach(textApart)
    m['Subject']='revert '+title
    
    server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
    #server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr.split(','), m.as_string())
    server.quit()





