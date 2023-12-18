from bottle import post, response, request
import x
@post("/renew-cookie")
def _():
    try:
        db = x.db()
        user_id = request.forms.user_id.strip()
        cookie_value = x.get_cookie_user()
        if user_id == cookie_value['user_id']:
            x.set_cookie_user(cookie_value)
        db.commit()
        return {"info":"ok","message":"Session updated"}
    except Exception as e:
        print(e.args[1])
        if "db" in locals(): db.rollback()
        response.status = e.args[0]
        return {"info":"error","errortype":str(e.args[0])}
    finally:
        if "db" in locals(): db.close()