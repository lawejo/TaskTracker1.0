from bottle import default_app, get, post, request, response, run, static_file
### Routes
import routes.render_index
import routes.render_task
import routes.render_verification
import routes.render_sign_up
import routes.render_login
import routes.render_profile


## Apis
import apis.api_sign_up
import apis.api_login
import apis.api_reset_password
import apis.api_update_user

##############################
##### Så den kan finde vores JS

@get("/js/<filename>")
def _(filename):
    return static_file(filename, "js")

#############################s#
##### Så den kan finde billeder

@get("/images/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./assets")


@get("/assets/<filename:re:.*\.JPG>")
def _(filename):
    return static_file(filename, root="./assets")


@get("/assets/<filename:re:.*\.jpeg>")
def _(filename):
    return static_file(filename, root="./assets")



@get("/assets/<filename:re:.*\.png>")
def _(filename):
    return static_file(filename, root="./assets")


@get("/assets/<filename:re:.*\.svg>")
def _(filename):
    return static_file(filename, root="./assets")


@get("/assets/<filename:re:.*\.png>")
def _(filename):
    return static_file(filename, root="./assets")

#############################
##### Så den kan finde CSS


@get("/output.css")
def _():
    return static_file("output.css", root=".")


# Import Apis
import apis.api_create_task
import apis.api_delete_task
import apis.api_edit_task


#############################

try:
    import production
    application = default_app()
except Exception as ex:
    print("Running local server")
    run(host="127.0.0.1", port=3000, debug=True, reloader=True, )
