# -*- coding:utf-8 -*-
# Author: cslzy
# Email: lizhenyang_2008@163.com
# Description:send something to someone.
# Date: 20151104 18:33:08
import smtplib
from email.mime.text import MIMEText as mt

# some information should be changed to you own
mail_host = "you email server such as: smtp.163.com" # set you mail host
host_user = "chang to you email address as a host, such as: lizhenyang_2008@163.com" # host to send email
host_password = "XXXXXthis is not useableXXXXXXchang to you own" # password of host

email_subject = "test message" # the subject of you email


reciever_address = "such as: lizhenyang_2008@163.com" #
send_message = "This is a test. oops..."



def sendTo(address, message):
    msg = mt(message, _subtype='plain')
    msg['Subject'] = email_subject
    msg['Form'] = host_user
    msg['To'] = address
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(host_user, host_password)
        server.sendmail(host_user, address, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

if __name__ == '__main__':
    sendTo(reciever_address,send_message)


