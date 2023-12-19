from bottle import get, post, request, response
import x
import bcrypt
from dotenv import load_dotenv
import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


@post("/reset-password")
def send_reset_email():
    try:
        db = x.db()
        user_email = request.forms.get("user_email")
        salt = bcrypt.gensalt()
        user_password = bcrypt.hashpw(x.validate_user_password().encode("utf-8"), salt)
        user = db.execute("SELECT * FROM users WHERE user_email = ? LIMIT 1", (user_email,)).fetchone()
        if user:
            user_inactive = 1
            db.execute("UPDATE users SET user_password = ?, user_inactive = ? WHERE user_email = ?", (user_password, user_inactive, user_email)).rowcount
            db.commit()
            password_resetting(user_email, user["user_firstname"])
        return {"info reset":"Succesfully sent reset password email"}
    except Exception as ex:
        return ex
    finally:
        if "db" in locals(): db.close()


@get("/reset-password/<user_firstname>")
def reset_password(user_firstname):
    try:
        db = x.db()
        user_inactive = 0
        rows_affected = db.execute("UPDATE users SET user_inactive = ? WHERE user_firstname = ?", (user_inactive, user_firstname)).rowcount
        db.commit()
        if not rows_affected:
            raise Exception("User not found")
        response.set_header("Location", "/")
        response.status = 302
        return response.body
    except Exception as e:
        print(e)
        if "db" in locals(): db.rollback()
        return {"info": str(e)}
    finally:
        if "db" in locals(): db.close()


def password_resetting(user_email, user_firstname):
    sender_email = "fulldemo93@gmail.com"
    receiver_email = user_email
    password = "iwzoxytyzkhwuqqu"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Password reset"
    message["From"] = sender_email
    message["To"] = receiver_email
    try:
        import production
        url = os.getenv("PYTHONANYWHERE_URL") + "/reset-password"
    except:
        url = "http://127.0.0.1:5858/reset-password"
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

    <h1 style="color: #4285f4;">TaskTrackr</h1>
    
    <p style="font-size: 16px;">Hey! It seems you want to reset your password.</p>
    
<a href={url}/{user_firstname} style="display: inline-block; background-color: #4285f4; color: #ffffff; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Reset Password</a>

    <p style="font-size: 14px; margin-top: 20px;">If you can't click the link above, copy and paste the following URL into your browser: {url}/{user_firstname}</p>

    <p style="font-size: 14px; margin-top: 20px;">Thank you for choosing TaskTrackr. We're excited to have you here!</p>

    <p style="font-size: 12px; color: #ccc;">This email was sent by TaskTrackr. Please do not reply to this email.</p>

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