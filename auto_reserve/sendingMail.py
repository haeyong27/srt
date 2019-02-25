# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText

class Mail:
    def __init__(self, text):
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()      # say Hello
        smtp.starttls()  # TLS 사용시 필요
        smtp.login('godyd2702@ajou.ac.kr', 'Sphv84031!@')
        
        msg = MIMEText(text)
        msg['Subject'] = 'srt 예약 완료'
        msg['To'] = 'ghkdgodydzz@gmail.com'
        smtp.sendmail('godyd2702@ajou.ac.kr', 'ghkdgodydzz@gmail.com', msg.as_string())
    
        smtp.quit()