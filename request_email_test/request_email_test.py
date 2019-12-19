import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
import sys

url = 'http://rsj.ningbo.gov.cn/col/col18843/index.html'
my_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"

# 发送邮箱服务器，账号，授权码，
mail_server = "smtp.163.com"
mail_user = "xx@163.com"
mail_pwd = "xx"

# 接收邮件
sender = mail_user
receivers = '236842785@qq.com'  

def get_str():
    response = requests.get(url,headers={'User-Agent': my_agent})
    print("get response ", response.status_code)

    txt = str(response.content.decode('utf-8'))
    start = txt.find("<recordset>")
    end = txt.find("</recordset>")
    txt = txt[start : end]

    ret = ""
    list = txt.split('</a>')
    # 只显示最新的5条
    for note in list[:5]:
        begin = note.find("html\">")
        temp = note[begin + 6:]
        ret = ret + temp + '\r\n\r\n'

    ret = ret + "\r\n详细见网站\r\nhttp://rsj.ningbo.gov.cn/col/col18843/index.html"
    return ret

def get_html():
    response = requests.get(url,headers={'User-Agent': my_agent})
    print("get response ", response.status_code)

    txt = str(response.content.decode('utf-8'))
    start = txt.find("<recordset>")
    end = txt.find("</recordset>")
    txt = txt[start : end]

    # 获取最新的发布网站的url
    ret = ""
    list = txt.split('</a>')
    begin = list[0].find("href=")
    end = list[0].find(".html")
    sub_url = list[0][begin+6: end] + '.html'
    new_url = "http://rsj.ningbo.gov.cn" + sub_url
    print("get url: ", new_url)

    # 获取最新的发布网站
    response2 = requests.get(new_url,headers={'User-Agent': my_agent})
    print("get response ", response2.status_code)
    ret = str(response2.content.decode('utf-8'))
    # 修改超链接地址，在邮件中可以直接前网站
    ret = ret.replace("/col/col", "http://rsj.ningbo.gov.cn/col/col")
    return ret, new_url

# 发送文字
def send_str(content):
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8')
    message['from'] = mail_user   # 发送者
    message['to'] =  receivers   # 接收者

    # 标题
    subject = '孙启梁，宁波事业单位招人更新'
    message['Subject'] = Header(subject, 'utf-8')
    
    try:
        smtpObj = smtplib.SMTP_SSL(mail_server, 465) 
        # smtpObj.set_debuglevel(1)
        smtpObj.login(mail_user,mail_pwd)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")

# 发送html
def send_html(html):
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(html, 'html', 'utf-8')
    message['from'] = mail_user   # 发送者
    message['to'] =  receivers   # 接收者

    # 标题
    subject = '孙启梁，宁波事业单位招人更新'
    message['Subject'] = Header(subject, 'utf-8')
    
    try:
        smtpObj = smtplib.SMTP_SSL(mail_server, 465) 
        # smtpObj.set_debuglevel(1)
        smtpObj.login(mail_user,mail_pwd)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")


if __name__ == "__main__":

    ret = ""
    last_url = ""

    # response = requests.get(url,headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"})
    # print("get response ", response.status_code)
    # print(response.content.decode('utf-8'))

    while True:
        # 获取最新的发布通知
        localtime = time.strftime( "%Y-%m-%d %H:%M:%S" ,time.localtime(time.time()) )
        print("---- now time :", localtime)
        
        try:
            ret, new_url = get_html()
            if (new_url != last_url):
                send_html(ret)
            last_url = new_url
            
        except:
            print("get html error.")
        
        time.sleep(60*60)



