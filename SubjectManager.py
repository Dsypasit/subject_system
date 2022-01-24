import smtplib, ssl
import time

class SubjectManager:
    def __init__(self):
        self.email = "ong.pasit@gmail.com"
        self.password = "erwijuehpnvbkeih"
        self.port = 465
    
    def get_message(self, subject, teacher, link, time):
        header = f"Subject: Get up! {subject} is comming!!"
        return header+"""\n

            Time: %s\n
            Teacher: %s\n
            Link: %s\n\n
            Good luck have fun!! :)
            """ %(time, teacher, link)

    def send_email(self, subject, teacher, link, time):
        # Create a secure SSL context
        context = ssl.create_default_context()
        message = self.get_message(subject, teacher, link, time)
        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=context) as server:
            server.login(self.email, self.password)
            server.sendmail(self.email, self.email, message)
            # TODO: Send email here

if __name__ == "__main__":
    manager = SubjectManager()
    manager.send_email("Digital and analog", "sopon", "www.youtube.com", "12:00")
    a = 0
    while True:
        a+=1
        print(a)
        time.sleep(0.5)
