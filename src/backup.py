# !/root/anaconda/bin/python
# encoding:utf8
# 代码存在问题，不要直接使用
'''
定时任务自动执行Python脚本，备份数据并上传至七牛云存储同时发送邮件通知
'''
import zipfile
import os
import qiniu
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header
from qiniu import Auth, BucketManager


def rm_old_backupfile(del_time, dir_name, q, bucket_name):
    bucket = BucketManager(q)
    filelist = os.listdir(dir_name)
    for f in filelist:
        f_info = os.stat(dir_name + '/' + f)
        # print f_info;
        if ((time.time() - f_info.st_mtime) > del_time):
            os.remove(dir_name + '/' + f)
            ret, info = bucket.delete(bucket_name, f)
            # delete the file on qiniu


def zip_dir(dirname, zipfilename):
    # print dirname+'****'+zipfilename
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    zf.write(dirname)
    zf.close()


def sendmail(re_mail, msg):
    mail_host = "smtp.mxhichina.com"
    mail_user = "srv@aiaifly.com"
    mail_pass = "xx"
    sender = "srv@aiaifly.com"
    receives = [re_mail]
    msg = MIMEText(
        time.strftime('%Y-%m-%d') + '数据库备份' + str(msg), 'plain', 'utf-8')
    msg['From'] = '晓庄档案助手'
    msg['To'] = re_mail
    subject = 'Backup Database successfully'
    msg['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        # smtpObj.set_debuglevel(1)
        smtpObj.connect(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receives, msg.as_string())
        smtpObj.quit()
        print("Send mail successfully!")
    except Exception as err:
        print(err)


if __name__ == '__main__':
    access_key = 'xx'
    secret_key = 'xx'
    bucket = 'njxzc'
    bucket_domain = 'http://p4hgtvptk.bkt.clouddn.com'
    # 替换自己的配置
    dir_name = '/mnt/backup/mysql_backup_data'
    file_zip = dir_name + '/Myslq_backup' + time.strftime('%Y-%m-%d') + '.zip'
    file_sql = dir_name + '/all.' + time.strftime('%Y-%m-%d') + '.sql'
    # 邮箱地址
    re_mail = '413659846@qq.com'
    save_data_time = 15 * 3600
    # 15days
    try:
        # 备份MYSQL数据
        os.system(
            '''
            mysqldump -u*root* -p*njxzc!QAZ*
                --all-databases > /mnt/backup/mysql.$(date +%Y-%m-%d).sql
            '''
        )
        # time.sleep(10)
        zip_dir(file_sql, file_zip)
        q = Auth(access_key, secret_key)
        token = q.upload_token(bucket)
        ret, info = qiniu.put_file(
            token, 'Myslq_backup' + time.strftime('%Y-%m-%d') + '.zip',
            file_zip)
        rm_old_backupfile(save_data_time, dir_name, q, bucket)
        sendmail(re_mail, '成功！')
        sendmail('', '成功！')
    except Exception as err:
        sendmail(re_mail, '失败！')
        sendmail('', '失败!' + str(err))
        print(err)
