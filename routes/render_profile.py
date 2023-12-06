from bottle import get, template
##############################
@get("/profile")
def _():

    return template("profile")
