from bottle import get, template
import x
##############################
@get("/sign-up")
def _():
    x.set_headers()
    return template("sign-up")
