import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import x
########################################


def email_sign_up(receiver_email, user_verification_key):
    sender_email = "fulldemo93@gmail.com"
    receiver_email = receiver_email
    password = "iwzoxytyzkhwuqqu"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Verification email"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
                Hi,
                How are you?
                www.your_website_here.com"""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to TaskTrackr</title>
</head>
<body style="font-family: 'Arial', sans-serif; background: #2D2D35; background: linear-gradient(180deg, #2D2D35 0%, #000000 80%, #000000 100%); color: #ffffff; padding: 20px; text-align: center;">

    <h1 style="color: #4285f4;">TaskTrackr Solutions</h1>
    
    <p style="font-size: 16px;">Welcome to TaskTrackr! Verify your email address to get started.</p>
    
<a href={x.EMAIL_AHREF}/verification/{user_verification_key} style="display: inline-block; background-color: #4285f4; color: #ffffff; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Verify Email</a>

    <p style="font-size: 14px; margin-top: 20px;">If you can't click the link above, copy and paste the following URL into your browser: {x.EMAIL_AHREF}/verification/{user_verification_key}</p>

    <p style="font-size: 14px; margin-top: 20px;">Thank you for choosing TaskTrackr Solutions. We're excited to have you on board!</p>

    <p style="font-size: 12px; color: #ccc;">This email was sent by TaskTrackr Solutions. Please do not reply to this email.</p>

</body>
</html>
 """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
