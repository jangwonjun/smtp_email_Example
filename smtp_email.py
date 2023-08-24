import smtplib
from email.mime.text import MIMEText

class Send_Email:
  
  '''
  KOR/ENGLISH

  Send_Email(보낼 메일주소, 메일 전송 제목, 전송 내용)
  Send_Email(SEND_EMAIL_ADDRESS, MAIL_TITLE, MAIL_CONTEXT)
   Example : (admin@test.com, TEST, This Is Ths TesT Message!)

  사용전에 MY_ACCOUNT, MY_PASSWORD에 구글 계정과 비밀번호를 입력하십시오.
  Please Before Using This Code! Fill The Blank MY_ACCOUNT AND MY_PASSWORD 
  
  안전한 사용을 위해서 ENV파일을 이용하여 계정을 보호하십시오!

  '''


  def __init__(self,mail,index ,contents):
    self.mail = mail
    self.index = index
    self.contents = contents
    MY_ACCOUNT = "#"
    MY_PASSWORD = "#"

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(MY_ACCOUNT, MY_PASSWORD)

    msg = MIMEText(index)
    msg['Subject'] = contents

    smtp.sendmail(MY_ACCOUNT, mail, msg.as_string())

    smtp.quit()
    
Send_Email("#","#","#")