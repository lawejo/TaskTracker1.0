from bottle import get, template
import x
##############################
@get("/login")
def _():
    user_cookie = x.get_cookie_user()
    return template("login", user_cookie=user_cookie)
