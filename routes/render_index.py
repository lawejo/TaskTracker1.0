from bottle import get, template, response, request
import traceback
import x
##############################

@get("/")
def render_index():

    try:
     
        user_cookie = x.get_cookie_user()
        x.set_headers()
        return template("index", user_cookie=user_cookie)
    except Exception as ex:
        traceback.print_exc()
        response.status = 500
        return {"info": str(ex)}
    finally:
        pass
