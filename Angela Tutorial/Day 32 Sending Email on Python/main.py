import smtplib
import datetime as dt
import random
MY_EMAIL = "benardbiidocuments@gmail.com"
MY_PASSWORD = "bcjzttnbwnverfli"
OTHER_ADDRESS= "benardbill@yahoo.co.uk"

#my_email = "benardbiidocuments@gmail.com"
#my_password = "bcjzttnbwnverfli"

#with smtplib.SMTP("smtp.gmail.com") as connection:
    #connection.starttls()
    #connection.login(user=my_email, password=my_password)
    #connection.sendmail(from_addr=my_email, to_address="benardbill@yahoo.co.uk", msg="subject:hello\n\n"
                                                                               #"This is the body of my email")

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs= OTHER_ADDRESS,
                            msg=f"subject: Daily Motivation\n\n {quote}")