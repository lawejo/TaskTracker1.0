from bottle import get, template
import x
##############################
@get("/login")
def _():
    # x.set_headers()
    return template("login")
