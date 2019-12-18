import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

message= MIMEMultipart()   

message["From"] = "info@ttyazilim.net"  #Mail'i gönderen kişi

message["To"] = "tunahancakil@gmail.com"    #Mail'i alan kişi

message["Subject"] = "Python Smtp ile Mail Gönderme" #Mail'in konusu


body= """

Python üzerinde smtp modülü
kullanarak mail gönderiyorum.

"""   #Mail içerisinde yazacak içerik


body_text = MIMEText(body,"plain") #

message.attach(body_text)

#Gmail serverlerine bağlanma işlemi.
try:
    mail = smtplib.SMTP("smtp.ttyazilim.net",587)  

    mail.ehlo()

    mail.starttls()    

    mail.login("Mail adresiniz","Şifreniz")

    mail.sendmail(message["From"],message["To"],message.as_string())

    print("Mail Başarılı bir şekilde gönderildi.")

    mail.close()
#Eğer mesaj gönderirken hata ile karşılaşırsak except çalışır.
except:
    sys.stderr.write("Bir hata oluştu. Tekrar deneyin...")
    sys.stderr.flush()