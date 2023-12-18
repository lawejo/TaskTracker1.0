from bottle import get, template, response, request
import traceback
import x
##############################

@get("/admin")
def render_index():

    try:
        db = x.db()
        user_cookie = x.get_cookie_user()
        if not user_cookie:
            return template("cookie-expired")

        if user_cookie['user_role'] == '1':
            return template("comp-access-denied", message='Access denied')
        users = db.execute("SELECT * FROM users").fetchall()
        return template("admin", users=users, user_cookie=user_cookie)
    except Exception as ex:
        traceback.print_exc()
        response.status = 500
        return {"info": str(ex)}
    finally:
        pass
