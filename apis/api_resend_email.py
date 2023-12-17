from bottle import post, response, request
import emails.email_sign_up as email
import x
@post("/api-resend-email")
def _():
    try:
        
        db = x.db()
        user_email = request.forms.resendEmail.strip()
        user_verify = db.execute('SELECT user_email, user_verification_key, user_verified_at FROM users WHERE user_email = ?',(user_email,)).fetchone()
        if user_verify != None and user_verify["user_verified_at"] == "0":
            email.email_sign_up(user_verify['user_email'], user_verify['user_verification_key'])
        db.commit()
        return {"info":"ok","message":"If the email exists in the database, you will receive an email shortly"}
    except Exception as e:
        print(e.args[1])
        if "db" in locals(): db.rollback()
        response.status = e.args[0]
        return {"info":"error","errortype":str(e.args[0])}
    finally:
        if "db" in locals(): db.close()