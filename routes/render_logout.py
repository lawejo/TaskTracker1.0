from dotenv import set_key
from bottle import get, response
import x
import traceback

@get("/logout")
def _():
    try:
        x.set_headers()
        response.status = 303
        response.delete_cookie("user", secret=x.COOKIE_SECRET)
        return{"info":"ok", "message":"Logout succesfull"}
    except Exception as e:
        traceback.print_exc(e)
        response.status = 400
        return {"info": "error", "errortype": str(e)}
    finally:
        pass
