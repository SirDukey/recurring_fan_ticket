
import smtplib

def send_mail():
    log_msg = 'Please import the latest db archive from prod to db2'
    mail_srv = 'mail.novusgroup.co.za'
    mail_port = '25'
    mail_name = 'itmonitor@novusgroup.co.za'
    mail_recip = ['helpdesk@novusgroup.co.za']
    mail_sub = 'Archive db import'
    mail_msg = 'Subject: {0}\n\n{1}'.format(mail_sub, log_msg)
    smtpServ = smtplib.SMTP(mail_srv, mail_port)
    smtpServ.sendmail(mail_name, mail_recip, mail_msg)
    smtpServ.quit()
    
if __name__ == '__main__':
    send_mail()
