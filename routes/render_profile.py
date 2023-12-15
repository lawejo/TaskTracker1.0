from bottle import get, template, request
import x
import os
from dotenv import load_dotenv
##############################
@get("/profile")
def _():
    try:
        db = x.db()
        user_cookie = x.user()
        user_cookie = request.get_cookie("user", secret=os.getenv('COOKIE_SECRET'))
        if not user_cookie:
            raise Exception("No cookie detected")
        return template("profile", user_cookie = user_cookie)
    except Exception as e:
        print(e)
    finally:
        if "db" in locals():
            db.close()

