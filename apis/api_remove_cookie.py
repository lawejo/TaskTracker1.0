from bottle import post, response, request
import x

@post("/remove-cookie")
def _():
    try:
        db = x.db()
        user_id = request.forms.user_id.strip()
        cookie_value = x.get_cookie_user()
        if user_id == cookie_value['user_id']:
            x.remove_cookie()
        db.commit()
        return {"info":"ok","message":"Cookie removed"}
    except Exception as e:
        if "db" in locals(): db.rollback()
        response.status = e.args[0]
        return {"info":"error","errortype":str(e.args[0])}
    finally:
        if "db" in locals(): db.close()