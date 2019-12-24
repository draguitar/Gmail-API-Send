# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 15:53:20 2019

@author: C09700
"""
import ezgmail
import datetime 
import configparser
config = configparser.ConfigParser()
config.read("config.ini")

MAIL_LIST = config['main']['to']

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
ezgmail.init(tokenFile='token.json', credentialsFile='credentials.json')

ezgmail.EMAIL_ADDRESS = 'from@gmail.com'
email = MAIL_LIST
subject = 'FTP SPEED download/upload report'
text = 'Dears,\n\t{}\n\tFTP SPEED download/upload report:'.format(current_time)

ezgmail.send(email, subject, text, ['test1.txt', 'test2.txt'])