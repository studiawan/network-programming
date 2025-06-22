import smtplib
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your Gmail credentials
GMAIL_USER = input("Enter your Gmail address: ").strip()
GMAIL_PASSWORD = getpass.getpass(prompt='Enter your Gmail password: ')

# Recipient email and name
recipient_email = input("Enter the recipient's email address: ").strip()
recipient_name = input("Enter the recipient's name: ").strip()

# Email subject
subject = "Ini adalah subjek email"

# Email body
pesan = f"""
    
Ini adalah isi email yang dikirim menggunakan Python.
Silakan sesuaikan dengan kebutuhan Anda."""

# Gmail SMTP setup
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Connect to server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(GMAIL_USER, GMAIL_PASSWORD)

# Create the email
msg = MIMEMultipart()
msg['From'] = "Name Pengirim"
msg['To'] = recipient_email
msg['Subject'] = subject

body = f"Dear {recipient_name},{pesan}"
msg.attach(MIMEText(body, 'plain'))

# Send the email
text = msg.as_string()
server.sendmail(GMAIL_USER, recipient_email, text)
print(f"Email sent to {recipient_email}")

# Close the connection
server.quit()