import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
mail_server = "smtp.163.com"
mail_user = "yywbxgl@163.com"
mail_pwd = "xxxx"

sender = 'yywbxgl@163.com'
receivers = '236842785@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('你好，孙启梁，请查收邮件..... ，', 'plain', 'utf-8')
message['from'] = mail_user   # 发送者
message['to'] =  receivers   # 接收者

# 标题
subject = '你好，孙启梁，请查收邮件'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP_SSL(mail_server, 465) 
    # smtpObj.set_debuglevel(1)
    smtpObj.login(mail_user,mail_pwd)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")