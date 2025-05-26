import csv
from email.message import EmailMessage
import smtplib


def get_credentials(filepath):
    with open(filepath, "r") as f:
        email_address = f.readline().strip()
        email_pass = f.readline().strip()
    return email_address, email_pass


def login(email_address, email_pass, server):
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email_address, email_pass)
    print("Logged in successfully.")


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    email_address, email_pass = get_credentials("credentials.txt")
    login(email_address, email_pass, server)

    subject = "Your Subject."
    body = (
        "Your Message.\n"
    )

    with open("emails.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            recipient = row[0].strip()
            message = EmailMessage()
            message.set_content(body)
            message['Subject'] = subject
            message['From'] = email_address
            message['To'] = recipient

            server.send_message(message)
            print(f"Sent to: {recipient}")

    server.quit()
    print("All emails have been sent.")


if __name__ == "__main__":
    send_mail()
