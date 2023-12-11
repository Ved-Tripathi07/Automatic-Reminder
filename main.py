from datetime import datetime
import random
import smtplib

MY_EMAIL = "tripathived2000@gmail.com"
MY_PASSWORD = "kftqnbmjptwfksti"
to_email = ["thenamantiwari07@gmail.com","alpana7061@gmail.com"]

current_time = datetime.now()
morning = current_time.replace(hour=8, minute = 1)
afternoon = current_time.replace(hour=12, minute = 30)
evening = current_time.replace(hour=17, minute = 10)
night = current_time.replace(hour=8, minute =1)

if current_time == morning:
    file_path = f"D:\\Interview modules\\SMTPLIB\\Reminder-Project\\morning\\letter_{random.randint(1,3)}.txt"
    with open(file_path, 'r') as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", "Alpana")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=to_email,
            msg=f"Subject:Good Morning Babe !\n\n{contents}"
        )


elif current_time == afternoon :
    file_path = f"D:\\Interview modules\\SMTPLIB\\Reminder-Project\\afternoon\\letter_{random.randint(1,3)}.txt"
    with open(file_path, 'r') as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", "Alpana")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=to_email,
            msg=f"Subject:Good Afternoon Babe !\n\n{contents}"
        )


elif current_time == evening :
    file_path = f"D:\\Interview modules\\SMTPLIB\\Reminder-Project\\evening\\letter_{random.randint(1,3)}.txt"
    with open(file_path, 'r') as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", "Alpana")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=to_email,
            msg=f"Subject:Good Evening Babe !\n\n{contents}"
        )

elif current_time == night :
    file_path = f"D:\\Interview modules\\SMTPLIB\\Reminder-Project\\night\\letter_{random.randint(1,3)}.txt"
    with open(file_path,'r') as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", "Alpana")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=to_email,
            msg=f"Subject:Good Night Babe !\n\n{contents}"
        )

else:
    print("Nothing sent")