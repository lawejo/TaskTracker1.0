from bottle import get, template, response, request
import traceback
import x
##############################

@get("/")
def render_index():

    try:
        x.set_headers()
        return template("index")
    except Exception as ex:
        traceback.print_exc()
        response.status = 500
        return {"info": str(ex)}
    finally:
        pass
