from bottle import default_app, get, post, request, response, run, static_file
### Routes
import routes.render_index
import routes.render_verification
## Apis
import apis.api_sign_up
import apis.api_login

##############################
##### Så den kan finde vores JS

@get("/js/<filename>")
def _(filename):
    return static_file(filename, "js")

#############################s#
##### Så den kan finde billeder

@get("/images/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./images")


@get("/images/<filename:re:.*\.JPG>")
def _(filename):
    return static_file(filename, root="./images")


@get("/images/<filename:re:.*\.jpeg>")
def _(filename):
    return static_file(filename, root="./images")



@get("/images/<filename:re:.*\.png>")
def _(filename):
    return static_file(filename, root="./images")



@get("/images/<filename:re:.*\.png>")
def _(filename):
    return static_file(filename, root="./images")

#############################
##### Så den kan finde CSS


@get("/output.css")
def _():
    return static_file("output.css", root=".")


#############################

try:
    import production
    application = default_app()
except Exception as ex:
    print("Running local server")
    run(host="127.0.0.1", port=2, debug=True, reloader=True, )
