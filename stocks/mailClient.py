import smtplib
class Mail():
    def __init__(self):
        self.mail = smtplib.SMTP("smtp.gmail.com",587)
        self.mail.ehlo()
        self.mail.starttls()
        self.email = "mattnappo@gmail.com"
        self.password = "JimiHendrix11"
    def send(self, subject, body):
        self.mail.login(self.email, self.password)
        content = "Subject: " + subject + "\n" + body
        self.mail.sendmail(self.email, self.email, content)
        self.mail.close()
email = Mail()
email.send("This is a test subject", "this is a very nice test body paragraph. This will make up the content of the email!")