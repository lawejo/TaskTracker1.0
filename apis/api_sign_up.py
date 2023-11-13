from bottle import post, request, response
import x
import traceback
import uuid
import time
@post("/api-sign-up")
def _():
    try:
        db = x.db()

        user_id = str(uuid.uuid4()).replace("-", "")
        user_created_at = int(time.time())
        user_firstname = x.validate_user_firstname()
        user_lastname = x.validate_user_lastname()
        user_email = x.validate_user_email()
        user_password = x.validate_user_password()
        user_confirm_password = x.validate_user_confirm_password()
        # user_birthday = 
        user_total_tasks = 0
        user_role = 0
        user_assigned_task_count = 0

        return {"ïnfo":"ok"}
    except Exception as e:
        print(e)
        if "db" in locals():
            db.rollback()
        traceback.print_exc()
        response.status = 400
        return {"info": "error", "errortype": str(e)}  
    finally:
        pass