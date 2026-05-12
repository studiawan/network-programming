# Prepare Gmail account
# Turn on 2-Step Verification in your Google account.
# Generate an App Password:
# Google Account -> Security -> App passwords -> select Mail -> generate (or just search App Passwords in Google Account settings)
# Use that 16-character app password in Python.

import smtplib
import csv
import sys
import time
import random
from email.message import EmailMessage
from email.utils import formataddr

# Define your Gmail credentials
GMAIL_USER = "your_gmail_user_here"
GMAIL_APP_PASSWORD = "your_app_password_here"

# Get the CSV file path containing email information from command line arguments
csv_file_path = sys.argv[1]

# read csv file and send email to each row
with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
    # Skip the header row and read the rest of the rows
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)  

    # Loop through each row in the CSV and send an email
    for row in reader:
        # TO_EMAIL = "hudan@its.ac.id"
        TO_EMAIL = f"{row[0]}@mail.edu"  # Assuming the email is constructed from the username in the first column

        # Create the email message
        msg = EmailMessage()
        msg["Subject"] = "This is a subject"
        msg["From"] = formataddr(("Your Name", GMAIL_USER))
        msg["To"] = TO_EMAIL
        msg.set_content(f"Yth. {row[1].strip()},\n\nThis is a message.\n\nUsername: {row[0]}\nPassword: {row[2]}\n\nThank you.")

        # Send the email using Gmail's SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            server.send_message(msg)
        
        # Sleep for a random interval between 1 and 120 seconds to avoid hitting rate limits
        interval = random.randint(1, 120)
        print(f"Email sent to {TO_EMAIL}. Sleeping for {interval} seconds.")
        time.sleep(interval)