from bottle import get, template
import x
##############################
@get("/sign-up")
def _():
    user_cookie  = x.get_cookie_user()
    x.set_headers()
    return template("sign-up", user_cookie=user_cookie)
