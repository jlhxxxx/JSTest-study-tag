#! python3
# sengEmail.py

import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpObj = smtplib.SMTP('smtp.qq.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('942900182@qq.com', 'password')  # 建议使用input输入密码

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] =  Header("测试", 'utf-8')
message['Subject'] = Header('标题', 'utf-8')
smtpObj.sendmail('942900182@qq.com', '12431145@qq.com', message.as_string())
# smtpObj.sendmail('942900182@qq.com', '12431145@qq.com', 'Subject: title\nfrom: tiger\nto: rabbit\nsdfsdgdfgdfg')
smtpObj.quit()