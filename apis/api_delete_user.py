from bottle import delete, response
import x
@delete("/delete-user")
def _():
    try:
        db = x.db()
        db.commit()
        return {"info":"ok","message":"User deleted"}
    except Exception as e:
        print(e)
        if "db" in locals(): db.rollback()
        response.status = 400
        return {"info":"error","errortype":str(e)}
    finally:
        if "db" in locals(): db.close()