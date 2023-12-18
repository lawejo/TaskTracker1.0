from bottle import post, request, response
import x
import traceback
import uuid
import time
import bcrypt
import emails.email_sign_up as email
@post("/api-sign-up")
def _():
    try:
        db = x.db()
        ###############
        user_id = str(uuid.uuid4()).replace("-", "")
        user_created_at = int(time.time())
        user_firstname = x.validate_user_firstname()
        user_lastname = x.validate_user_lastname()
        user_email = x.validate_user_email()
        user_password = x.validate_user_password()
        x.validate_user_confirm_password()
        user_tasks_created = 0
        user_role = 0
        user_assigned_task_count = 0
        user_verification_key = str(uuid.uuid4()).replace("-", "")
        user_verified_at = 0
        user_inactivation_key = str(uuid.uuid4()).replace("-", "")
        user_inactive = 0
        user_reset_key = str(uuid.uuid4()).replace("-", "")
        user_avatar = 0
        user_birthday = ""
        user ={
            "user_id": user_id,
            "user_created_at": user_created_at,
            "user_firstname": user_firstname,
            "user_lastname": user_lastname,
            "user_email": user_email,
            "user_password": bcrypt.hashpw(user_password.encode("utf-8"), bcrypt.gensalt()),
            "user_tasks_created": user_tasks_created,
            "user_assigned_task_count": user_assigned_task_count,
            "user_role": user_role,
            "user_verification_key": user_verification_key,
            "user_verified_at": user_verified_at,
            "user_inactivation_key": user_inactivation_key,
            "user_inactive": user_inactive,
            "user_reset_key": user_reset_key,
            "user_avatar": user_avatar,
            "user_birthday": user_birthday
        }
     
        values = ""
        for key in user:
            values += f":{key},"
        values = values.rstrip(",")
        total_rows_inserted = db.execute(
            f"INSERT INTO users VALUES({values})", user).rowcount
        if total_rows_inserted != 1:
            raise Exception("Please, try again")
        
        email.email_sign_up(user_email, user_verification_key)
        db.commit()
       
        return {"info":"ok", "message": "Your sign-up is complete. Please check your email to verify and enjoy full access to our services."}
    except Exception as e:
        if "db" in locals():
            db.rollback()
        traceback.print_exc()
        response.status = 400
        return {"info": "error", "errortype": str(e)}  
    finally:
        if "db" in locals():
            db.close()