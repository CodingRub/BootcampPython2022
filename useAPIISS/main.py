import requests
import smtplib
from datetime import datetime
from test2 import sendemail

MY_LAT = 48.957980 # Your latitude
MY_LONG = 2.881200 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print((iss_latitude, iss_longitude))
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

#Your position is within +5 or -5 degrees of the ISS position.

def is_night():
    res = False
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        res = True
    return res 

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
if not is_night():
    print("Il fait jour !")
else:
    print("Il fait nuit")

if is_iss_overhead() and not is_night():
    sendemail("rub77indy@outlook.fr", "r16s22j29", "rubstr@protonmail.com", "Look up !", "The ISS is above you! However, you will have difficulty seeing it because of the sun :(")
else:
    print("Nope")
if is_iss_overhead() and is_night():
    sendemail("rub77indy@outlook.fr", "r16s22j29", "rubstr@protonmail.com", "Look up !", "The ISS is above you! Get your telescope out quickly or try to take a picture of it!")
else:
    print("Nope")

