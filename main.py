import smtplib
import time
import requests
from datetime import datetime

my_email = "codelearner5582@gmail.com"
password = "lamxgcjapocohtfa"

MY_LAT = 16.591040 # Your latitude
MY_LONG = 81.520782 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# MY_LAT = iss_latitude
# MY_LONG = iss_longitude

#Your position is within +5 or -5 degrees of the ISS position.


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


while True:
    time.sleep(60)
    if MY_LAT+5 >= iss_latitude or MY_LAT-5 <= iss_latitude  and MY_LONG+5 >= iss_longitude or MY_LONG-5 <= iss_longitude and time_now >= sunset or time_now <= sunrise:
        with smtplib.SMTP("smtp.gmail.com",port = 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="nikhilnethala8@gmail.com", msg=f"Subject:ISS Near to U\n\nLookUp!!")





