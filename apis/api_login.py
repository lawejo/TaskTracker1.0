from bottle import post, request, response
import x
import bcrypt


@post("/api-login")
def _():
    try:
        error_message = "Invalid credentials"
        db = x.db()
        user_email = request.forms.get('user_email').strip()
        user_password = request.forms.get('user_password').strip()
       
        cookie_user = db.execute(
                "SELECT * FROM users WHERE user_email = ?", (user_email,)).fetchone()
     
    
        if not cookie_user:
            raise Exception(400, error_message)
  
        if not bcrypt.checkpw(user_password.encode("utf-8"), cookie_user["user_password"]):
             raise Exception(400, error_message)
    
        if cookie_user["user_verified_at"] == "0":
            raise Exception(
                "Your account has yet to be verified, please check your email too complete your account.")
 
        if cookie_user["user_inactive"] == "1":
            print(cookie_user)
            raise Exception(
                "It appears you deleted your account. Contact support to have your account retrieved.")
   
        x.set_cookie_user(cookie_user)
        return {"info": "ok", "message": "You will be redirected shortly."}
    except Exception as e:
        print(e)
        try:
            response.status = e.args[0]
            return {"info": "error", "errortype": e.args[1]}
        except:
            response.status = 500
            return {"info": "error", "errortype": str(e)}
    finally:
        if "db" in locals():
            db.close()
