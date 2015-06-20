#!/usr/bin/python

import smtplib
import ntpath
import sys
import getopt
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase

def sendMail(params):
    emailfrom = "geotomunifr@gmail.com"
    emailto=params['to'];
    if 'files' in params:
        filesToSend = params['files']
        
    if 'subject' in params:
        subject=params['subject']
    else:
        subject="Geotom Mail"
        
    username = "geotomunifr"
    password = "6%62sdg34tw"
    
    msg = MIMEMultipart()
    msg["From"] = emailfrom
    msg["To"] = ", ".join(emailto)
    msg["Subject"] = subject
    msg.preamble = subject
    
    for fileSend in filesToSend:
        fp = open(fileSend, "rb")
        attachment = MIMEBase('application', "octet-stream")
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=ntpath.basename(fileSend))
        msg.attach(attachment)
    
    server = smtplib.SMTP("smtp.gmail.com:587",timeout=50)
    server.starttls()
    server.login(username,password)
    server.sendmail(emailfrom, emailto, msg.as_string())
    server.quit()

def main():
    myopts, args = getopt.getopt(sys.argv[1:],"f:s:t:")
    params=dict();
    params['to']=[]
    params['files']=[]
    for o, a in myopts:
        if o == '-f':
            params['files']=a.split(',')
        elif o == '-s':
            params['subject']=a
        elif o == '-t':
            params['to'].append(a)
        else:
            print("Usage")

    sendMail(params);
    

if __name__ == "__main__":
    main()
