from bottle import get, template, response, request
import traceback
import x
##############################

@get("/admin")
def render_index():

    try:
        db = x.db()
        user = x.get_cookie_user()
        if not user or not user['user_role'] == '1':
            return template("access-denied", message='Access denied')
        users = db.execute("SELECT * FROM users").fetchall()
        return template("admin", users=users)
    except Exception as ex:
        traceback.print_exc()
        response.status = 500
        return {"info": str(ex)}
    finally:
        pass
