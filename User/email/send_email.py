import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_address = "ProtoCat v5 <protocat.user@gmail.com>"
to_address = ""
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = "SMTP Test"
msg.attach(MIMEText("Here is a test for text", 'plain'))
msg.attach(MIMEText('<a href = "http://www.python.org">Link</a>', 'html'))

try:
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login("protocat.user@gmail.com", "")
    smtpObj.sendmail(from_address, to_address, msg.as_string())
    smtpObj.quit()
    print("Sent email")
except SMTPException:
    print("Unable to send email")