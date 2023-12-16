from bottle import response, put, request
import x

@put("/api-admin-update-user")
def _():
    try:
        db = x.db()
        userId = request.forms.user_id
        cookie_user = x.get_cookie_user()
        updated_user=""

       

        updated_firstname = x.validate_user_firstname()

        db.execute('UPDATE users SET user_firstname = ? WHERE user_id = ?',(updated_firstname, userId)).fetchone()
        
        
        updated_lastname = x.validate_user_lastname()
        db.execute('UPDATE users SET user_lastname = ? WHERE user_id = ?',(updated_lastname, userId)).fetchone()
  
        updated_user = db.execute('SELECT * FROM users WHERE user_id = ?',(userId,)).fetchone()

        if updated_user:
               [updated_user.pop(key) for key in x.keys_list]
 
 
        db.commit()
        return {"info":"ok","message":"User updates", "user":updated_user}
    except Exception as e:
        print(e.args[1])
        print('*'*40)
        if "db" in locals(): db.rollback()
        response.status = e.args[0]
        return {"info":"error","errortype":str(e.args[1])}
    finally:
        if "db" in locals(): db.close()