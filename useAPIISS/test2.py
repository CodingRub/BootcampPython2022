import smtplib

def sendemail(your_email: str, your_pwd: str, target: str, subject: str, your_msg: str):
    try:
        connection = smtplib.SMTP("outlook.office365.com")
        connection.starttls()
        connection.login(user=your_email, password=your_pwd)
    except smtplib.SMTPAuthenticationError:
        print("Authentification Error :(")
    else:
        message = 'Subject: {}\n\n{}'.format(subject, your_msg)
        connection.sendmail(from_addr=your_email, to_addrs=target, msg=message)
        connection.close()
        print("Email Send !")