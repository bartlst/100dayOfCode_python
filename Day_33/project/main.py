import requests
import smtplib
from datetime import datetime

MY_LATITUDE = 51.207576
MY_LONGITUDE = 16.151619
MY_EMAIL = "email@gmail.com"
MY_EMAIL_PASSWORD = "emailpassword"

def check_iss_pos():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    response.raise_for_status()
    iss_data = response.json()

    iss_latitude = float(iss_data['iss_position']['latitude'])
    iss_longitude = float(iss_data['iss_position']['longitude'])

    return MY_LONGITUDE-5 < iss_longitude < MY_LONGITUDE+5 and MY_LATITUDE - 5 < iss_latitude < MY_LATITUDE + 5


def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0
    }
    response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
    data = response.json()

    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    time_now = datetime.now()
    return time_now.hour >= sunset or time_now.hour <= sunrise


if check_iss_pos() and is_night():
    print("OK")
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs="second_email@gmail.com",
                        msg=f"Subject:Look UP!\n\n ISS is above you")
    connection.close()

