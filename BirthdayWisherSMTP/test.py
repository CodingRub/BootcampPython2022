import smtplib
from random import choice
import datetime as dt

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

def sendQuotes():
    now = dt.datetime.now()
    weekday = now.weekday()
    if weekday == 5:
        try:
            data_file = open("quotes.txt", "r")
        except FileNotFoundError:
            print("Data file doesn't exist :(")
        else:
            with data_file as quotes:
                all_quotes = quotes.readlines()
                quote = choice(all_quotes)
            sendemail("rub77indy@outlook.fr", "r16s22j29", "rubstr@protonmail.com", "Your Motivational Quote of the Week !", quote)

""" sendQuotes() """