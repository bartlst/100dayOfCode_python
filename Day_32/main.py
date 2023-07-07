import smtplib
import random
import datetime as dt

MY_EMAIL = "email@gmail.com"
MY_EMAIL_PASSWORD = "emailpassword"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 4:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        message = random.choice(quotes)
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs="second_email@gmail.com",
                        msg=f"Subject:Monday Motivation\n\n {message}")
    connection.close()



