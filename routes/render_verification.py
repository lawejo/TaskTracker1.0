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
        view = ''
        db = x.db()
        user_verification = db.execute("SELECT * FROM users WHERE user_verification_key = ?",(verificationkey,)).fetchone()
        if user_verification:
            db.execute("UPDATE users SET user_verified_at = '1' WHERE user_verification_key = ?",(verificationkey,)).fetchone()
            view = 'verification_succes'
            title = 'Verification succes'
        if not user_verification:
            view = 'verification_failed'
            title = 'Verification failed'
        db.commit()
        return template(view, title=title, verificationkey=verificationkey)
    except Exception as ex:
        print(ex)
        traceback.print_exc()
        return str(ex)
    finally:
        if "db" in locals():
            db.close()

        ##############################
