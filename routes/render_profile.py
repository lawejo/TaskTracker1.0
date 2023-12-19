from bottle import get, template, request
import x
from dotenv import load_dotenv
##############################
@get("/profile")
def _():
    try:
        db = x.db()
        user_cookie = x.get_cookie_user()
        if not user_cookie:
            return template('cookie-expired', user_cookie=user_cookie)
        x.set_headers()
        return template("profile", user_cookie = user_cookie)
    except Exception as e:
        print(e)
    finally:
        if "db" in locals():
            db.close()

