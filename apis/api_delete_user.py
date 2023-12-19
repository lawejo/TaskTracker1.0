from bottle import delete, response, request, template
import x
import bcrypt
@delete("/api-delete-user")
def _():
    try:
        error_admin = 'Failed to verify this admin user'
        error_target = 'Failed to locate this user in database'
        db = x.db()
        user = x.get_cookie_user()
        # Check for if they are logged in (cookie user) and if they are admin (user role = 1)
        if not user or not user['user_role'] == '1':
            return template("comp-access-denied", message='Access denied')  
        # Linje 15 er i tilfældet at en hacker får adgang til at sende formlen til serveren, men sender tomme felter med        
        if not request.forms.get('admin_password') or not request.forms.get('target_id'):
            raise Exception(400,'Form submission error. Please make sure all required fields are filled.')
        target_user_id =  request.forms.get('target_id').strip()
        admin_password = request.forms.get('admin_password').strip()

        verify_target = db.execute('SELECT COUNT(*) FROM users WHERE user_id = ?',(target_user_id,)).fetchone()
        logged_user_pw_db = db.execute("SELECT user_password FROM users WHERE user_id = ?",(user['user_id'],)).fetchone()
 
        if verify_target["COUNT(*)"] == 0:
            raise Exception(400, error_target)        
        if not bcrypt.checkpw(admin_password.encode("utf-8"), logged_user_pw_db["user_password"]):
             raise Exception(400, error_admin)
        user_firstname = db.execute('SELECT user_firstname FROM users WHERE user_id =?',(target_user_id,)).fetchone()
        db.execute('DELETE FROM users WHERE user_id = ?',(target_user_id,)).fetchone()
    
        db.commit()
        return {"info":"ok","message":"User deleted","user":user_firstname}
        
    except Exception as e:
        if "db" in locals(): db.rollback()
        response.status = e.args[0]
        return {"info":"error","errortype":str(e.args[1])}
    finally:
        if "db" in locals(): db.close()