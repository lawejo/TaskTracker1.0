from bottle import get, template, response, request
import os
import sqlite3
import pathlib
import x
import random
import traceback
##############################
@get("/verification/<verificationkey>")
def _(verificationkey):
    try:
        link = ''
        db = x.db()
        user_verification = db.execute("SELECT * FROM users WHERE user_verification_key = ?",(verificationkey,)).fetchone()
        if user_verification:
            db.execute("UPDATE users SET user_verified_at = '1' WHERE user_verification_key = ?",(verificationkey,)).fetchone()
            title = 'Verification succes'
            status = "Congratulations!"
            p1 = "Your account has been successfully verified. You can now access all the features of our platform."
            p2 = "Note: To ensure the security of your account, please log in using your credentials. Close this tab or use the following link"
        if not user_verification:
            title = 'Verification failed'
            status = "Verification failed"
            p1 = "We encountered an issue while verifying your account. Please ensure that you are using the correct verification link"
            link =" or click here to resend an email."
            p2 = "Note: For security reasons, do not attempt to use an expired or invalid verification link. If the issue persists, kindly reach out to our support team for further assistance."
        db.commit()
        return template('verification', title=title, p1=p1, p2=p2, status=status, link=link)
    except Exception as ex:
        print(ex)
        traceback.print_exc()
        return str(ex)
    finally:
        if "db" in locals():
            db.close()

        ##############################
