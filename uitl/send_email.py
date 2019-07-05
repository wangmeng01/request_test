#coding:utf-8
import smtplib
from email.mime.text import MIMEText
class Send_Email():
    global send_user
    global send_password
    global mail_host
    send_user='919218732@qq.com'
    send_password='csebcmranpytbbab'
    mail_host='smtp.qq.com'
    def send_email(self,user_list,sub,cotent):
        user="DTT"+"<"+send_user+">"
        message=MIMEText(cotent,_subtype='plain',_charset='utf-8')
        message['Subject']=sub
        message['From']=user
        message['To']=';'.join(user_list)
        server=smtplib.SMTP()
        server.connect(mail_host)
        server.login(send_user,send_password)
        server.sendmail(user,user_list,message.as_string())
        server.close()
    def send_main(self,pass_list,fail_list):
        pass_num=float(len(pass_list))
        fail_num=float(len(fail_list))
        count_num=pass_num+fail_num
        pass_result='%.2f%%'%(pass_num/count_num*100)
        fail_result = '%.2f%%' % (pass_num / count_num * 100)
        content="此次一共共运行接口数量%s个，通过个数为%s个，失败个数为%s个，通过率为%s，失败率为%s"%(count_num,pass_num,fail_num,pass_result,fail_result)
        user_list=['13552278611@163.com']
        sub='接口自动化测试报告'
        self.send_email(user_list,sub,content)
