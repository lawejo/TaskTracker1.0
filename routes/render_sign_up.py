from bottle import get, template
##############################
@get("/sign-up")
def _():

    return template("sign-up")
