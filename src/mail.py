import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header

re_mail = '413659846@qq.com'


def sendmail(re_mail, msg):
    mail_host = "smtp.mxhichina.com"
    mail_user = "srv@aiaifly.com"
    mail_pass = "xxx"
    sender = "srv@aiaifly.com"
    receives = [re_mail]
    msg = MIMEText(
        time.strftime('%Y-%m-%d') + '数据库备份' + str(msg), 'plain', 'utf-8')
    msg['From'] = '晓庄档案助手'
    msg['To'] = re_mail
    subject = 'Backup Database successfully'
    msg['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL()
        smtpObj.set_debuglevel(1)
        smtpObj.connect(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receives, msg.as_string())
        smtpObj.quit()
        print("Send mail successfully!")
    except Exception as err:
        print(err)


sendmail(re_mail, '成功')
