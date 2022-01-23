import smtplib, ssl

class SubjectManager:
    def __init__(self):
        self.email = "ong.pasit@gmail.com"
        self.password = "erwijuehpnvbkeih"
        self.port = 465
        self.message = """\
Subject: Hi there

This message is sent from Python."""

    def send_email(self):
        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=context) as server:
            server.login(self.email, self.password)
            server.sendmail(self.email, self.email, self.message)
            # TODO: Send email here

if __name__ == "__main__":
    manager = SubjectManager()
    manager.send_email()
