from bottle import default_app, get, post, request, response, run, static_file
### Routes
import routes.render_index
import routes.render_dashboard
import routes.render_task
import routes.render_verification
import routes.render_sign_up
import routes.render_login
import routes.render_logout
import routes.render_admin
import routes.render_profile

import routes.render_verification


## Apis
import apis.api_create_task
import apis.api_edit_task
import apis.api_delete_task
import apis.filter_task
import apis.api_sign_up
import apis.api_login
import apis.api_create_task
import apis.api_delete_task
import apis.api_edit_task
import apis.api_delete_user
import apis.api_admin_update_user
import apis.api_update_user
import apis.api_resend_email
import apis.api_renew_cookie
import apis.api_remove_cookie
import apis.api_reset_password
##Misc
import x
import git
import os
from dotenv import load_dotenv
load_dotenv()
# import apis.api_logout
# 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
# https://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@github.com/lawejo/tasktracker.git
@post('/'+os.getenv("GIT_HOOK"))
def git_update():
    repo = git.Repo('./mysite')
    origin = repo.remotes.origin
    repo.create_head('main', origin.refs.main).set_tracking_branch(
        origin.refs.main).checkout()
    origin.pull()
    return ""
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




#############################
if x.local() == False:
    run(host="127.0.0.1", port=5858, debug=True, reloader=True, )
else:
    import production
    application = default_app()


