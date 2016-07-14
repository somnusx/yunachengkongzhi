#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import subprocess
import poplib
import re
import time

email = "somnus_sx@sina.com"
password = "password"
pop3_server = "pop.sina.com"

last = []

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def print_info(msg, indent=0):
    if indent == 0:
        value = msg.get('Subject')
        if value:
            value = decode_str(value)
            if last:
                for la in last:                    
                    if value==la:
                        print('yes')                        
                    else:
                        last.pop()
                        last.append(value)
                        subprocess.Popen(value, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)                        
                
            else:
                last.append(value)
                subprocess.Popen(value, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

                             
def accept():

    server = poplib.POP3(pop3_server)

    server.user(email)

    server.pass_(password)

    resp, mails, octets = server.list()

    index = len(mails)

    resp, lines, octets = server.retr(index)

    msg_content = b'\r\n'.join(lines).decode('utf-8')

    msg = Parser().parsestr(msg_content)

    print_info(msg)

    server.quit()

while True:
    accept()
    time.sleep(5)



