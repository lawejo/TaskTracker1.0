from bottle import get, template, response, request
import traceback
##############################

@get("/")
def render_index():

    try:

      
        response.add_header(
            "Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        response.add_header("Pragma", "no-cache")
        response.add_header("Expires", 0)

        return template("index")
    except Exception as ex:
        traceback.print_exc()
        response.status = 500
        return {"info": str(ex)}
    finally:
        pass
