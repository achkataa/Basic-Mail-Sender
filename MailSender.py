import smtplib

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login("example", "example")
    subject = "Hello, World"
    body = "How are you today"

    msg = f"Subject: {subject}\n\n{body}"


    smtp.sendmail("example@gmail.com", "example@gmail.com", msg)
