# coding:utf-8
import smtplib
import arrow
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# file_path="D:\\搜狗高速下载\\20180119周报-盛轶骏.xlsx"
time=arrow.now().format('YYYY-MM-DD')
filetime=arrow.now().format(('MMDD'))
print (time)
print (filetime)
smtpserver="smtp.exmail.qq.com"
port=465
sender="yijun.sheng@bangbanglicai.com"
psw="Aa66512155!"
receiver="wenyan.chen@bangbanglicai.com"  #多个收件人这里设置
# receiver="496477498@qq.com"
subject="【周报】技术部-盛轶骏-"+str(time)+""
acc = 'dengting.zhang@bangbanglicai.com,ting.yu@bangbanglicai.com'
# acc = 'yijun.sheng@bangbanglicai.com'
#设定混合模式
msg = MIMEMultipart()
#正文
file='D:\pythonstudy\python3\\123.html'
f=open(file,'rb')
body = f.read() # 定义邮件正文为 html 格式
# body='1'
# print (body)
f.close()
msg1 = MIMEText(body, 'html', 'utf-8')
msg['from'] = sender
msg['to'] = "wenyan.chen@bangbanglicai.com"
# msg['to'] = "496477498@qq.com"
msg['Cc'] = acc  #抄送
msg['subject'] = subject


#附件
# 读取xlsx文件作为附件，open()要带参数'rb'，使文件变成二进制格式,从而使'base64'编码产生作用，否则附件打开乱码
xlsxpart = MIMEApplication(open("D:\\搜狗高速下载\\2018"+str(filetime)+"周报-盛轶骏.xlsx", 'rb').read())
basename = "2018"+str(filetime)+"周报-盛轶骏.xlsx"
xlsxpart.add_header('Content-Disposition', 'attachment', filename=('gbk', '', basename))#注意：此处basename要转换为gbk编码，否则中文会有乱码。
msg.attach(xlsxpart)
msg.attach(msg1)

print (receiver.split(',')+acc.split(','))
smtp=smtplib.SMTP()
smtp.connect(smtpserver)
smtp = smtplib.SMTP_SSL(smtpserver, port)
smtp.login(sender, psw) # 登录
smtp.sendmail(sender, receiver.split(',')+acc.split(','), msg.as_string()) # 发送
smtp.quit() # 关闭