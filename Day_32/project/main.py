##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



import pandas
import random
import smtplib
import datetime as dt

MY_EMAIL = "email@gmail.com"
MY_EMAIL_PASSWORD = "emailpassword"
LETTERS_TEMPLATE = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

birthdays_data = pandas.read_csv("birthdays.csv", )
birthdays_dict = birthdays_data.to_dict(orient="records")
for birthday in birthdays_dict:
    if birthday["month"] == dt.datetime.now().month and birthday["day"] == dt.datetime.now().day:
        letter = random.choice(LETTERS_TEMPLATE)
        with open("./letter_templates/"+letter) as file:
            message = file.read().replace("[NAME]", birthday['name'])
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="second_email@gmail.com",
                                msg=f"Subject:Happy Birthday!\n\n {message}")
            connection.close()
