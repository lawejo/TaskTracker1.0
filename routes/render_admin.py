from email import message
from math import exp
from bottle import get, template, response, request
import traceback
import x
##############################

@get("/admin")
def render_index():

    try:
        db = x.db()
        cookie_user = request.get_cookie("user", secret=x.COOKIE_SECRET)
        if not cookie_user or not cookie_user['user_role'] == '1':
            return template("access-denied", message='Access denied')
        users = db.execute("SELECT * FROM users WHERE NOT user_role = 0").fetchall()
        return template("admin", users=users)
    except Exception as ex:
        traceback.print_exc()
        response.status = 500
        return {"info": str(ex)}
    finally:
        pass
