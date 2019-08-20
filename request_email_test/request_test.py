import requests
# from requests_html import HTMLSession

url = 'http://rsj.ningbo.gov.cn/col/col18843/index.html'

response = requests.get(url)
# print(response)

txt = str(response.content.decode('utf-8'))
start = txt.find("<recordset>")
end = txt.find("</recordset>")
txt = txt[start : end]
# print(txt)

ret = ""

list = txt.split('</a>')
for note in list[:-1]:
    begin = note.find("html\">")
    temp = note[begin + 5:]
    ret = ret + temp + '\r\n'
    # print(temp)

ret = ret + "\r\n详细见网站\r\nhttp://rsj.ningbo.gov.cn/col/col18843/index.html"

print(ret)
