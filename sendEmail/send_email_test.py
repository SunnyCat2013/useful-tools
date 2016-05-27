# -*- coding:utf-8 -*-
# Author: cslzy
# Email: lizhenyang_2008@163.com
# Description: if the files number is enough, send email to me.
# Date: 20151104 18:52:45
from send_email import sendTo
import os
import time

flag = True

reciever_email = 'lizhenyang_2008@163.com' # you should change to you own
sleepy_time = 3 * 3600
print 'send message to %s every %d seconds'%(reciever_email, sleepy_time)

i = 0
while flag:
    i += 1
    print 'the %d\'th time to check'%i
    message = ''
    dirPath = '.'
    if os.path.exists(dirPath):
        listdir = os.listdir(dirPath)
        message += 'there are %d file in %s\n'%(len(listdir), dirPath)
    sendTo(reciever_email, message)
    # sleep
    time.sleep(sleepy_time)
