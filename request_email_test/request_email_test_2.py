import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from bs4 import BeautifulSoup
import time
import sys

url = 'https://www.nbpt.edu.cn/744/list.htm'
my_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"

# 发送邮箱服务器，账号，授权码，
mail_server = "smtp.163.com"
mail_user = "yywbxgl@163.com"
mail_pwd = "s65656645"

# 接收邮件
sender = mail_user
receivers = '236842785@qq.com'

# 获取公告列表
def get_list(html_doc):
    # html字符串创建BeautifulSoup对象
    #soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
    soup = BeautifulSoup(html_doc, 'html.parser')
    list = soup.find_all('a')
    ret = []
    for i in list:
        if (i.attrs.get('title')):
            # print(i.attrs)
            ret.append(i.attrs['title'])
    # print(ret)
    return ret

    
# 检测公告是否更细，发送邮件
def check_url(temp_list):

    response = requests.get(url,headers={'User-Agent': my_agent})
    print("get response ", response.status_code)
    
    txt = str(response.content.decode('utf-8'))
    # 解析通知列表
    new_list = get_list(txt)
    
    # 如果网站列表有更新，发送邮件
    if (new_list != temp_list):
        # 只显示最新的5条
        str_temp = ""
        for i in new_list[:1]:
            print(i)
            str_temp += i + "\r\n\r\n"
        str_temp += "\r\n\r\n详细见网站" + url
        send_str(str_temp)
        temp_list = new_list

    return temp_list


# 发送邮件文字
def send_str(content):
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8')
    message['from'] = mail_user   # 发送者
    message['to'] =  receivers   # 接收者

    # 标题
    subject = '孙启梁，大学老师更新'
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

    temp_list = []
    while True:
        # 获取最新的发布通知
        localtime = time.strftime( "%Y-%m-%d %H:%M:%S" ,time.localtime(time.time()) )
        print("---- now time :", localtime)

        try:
            temp_list = check_url(temp_list)
        except:
            print("get html error.")

        time.sleep(60*60)
        # time.sleep(15)




