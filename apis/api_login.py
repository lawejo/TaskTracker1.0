from bottle import post, request, response
import x
import bcrypt


@post("/api-login")
def _():
    try:
        db = x.db()
        user_email = request.forms.get('user_email')
        user_password = request.forms.get('user_password')
       
        user = db.execute(
                "SELECT * FROM users WHERE user_email = ?", (user_email,)).fetchone()
     
    
        if not user:
            raise Exception(400, "Wrong email or username")
        
        if not bcrypt.checkpw(user_password.encode("utf-8"), user["user_password"].encode()):
             raise Exception(400, "Invalid credentials")

        if user["user_verified_at"] == "0":
            raise Exception(
                "Your account has yet to be verified, please check your email too complete your account.")

        if user["user_inactive"] == "1":
            print(user)
            raise Exception(
                "It appears you deleted your account. Contact support to have your account retrieved.")
        try:

            import production
            is_cookie_https = True
        except:
            is_cookie_https = False
        response.set_cookie("user", user, secret=x.COOKIE_SECRET,
                            httponly=True)
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
