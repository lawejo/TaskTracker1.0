from bottle import get, template
import x
##############################


@get("/sign-up")
def _():

    return template("sign-up")
