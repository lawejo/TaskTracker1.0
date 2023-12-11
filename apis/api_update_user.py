from bottle import put, post, response, request
import os
import x
from dotenv import load_dotenv


@put("/update")
def update():
  try:
    db = x.db()
    user_cookie = x.user()
    user_id = user_cookie["user_id"]
    user_firstname = user_cookie["user_firstname"]
    user_lastname = user_cookie["user_lastname"]
    
    new_user_firstname = x.update_user_firstname()
    if user_firstname != new_user_firstname and new_user_firstname != "" and new_user_firstname is not None:
      db.execute(f"UPDATE users SET user_firstname = ? WHERE user_firstname = ?", (new_user_firstname, user_firstname))
      user_cookie["user_firstname"] = new_user_firstname

    new_user_lastname = x.update_user_lastname()
    if user_lastname != new_user_lastname and new_user_lastname != "" and new_user_lastname is not None:
      db.execute(f"UPDATE users SET user_lastname = ? WHERE user_lastname = ?", (new_user_lastname, user_lastname))
      user_cookie["user_lastname"] = new_user_lastname
    
    avatar = user_cookie["user_avatar"]
    new_avatar = x.avatar_picture()
    if avatar != user_id and new_avatar != "" and new_avatar is not None:
      db.execute(f"UPDATE users SET user_avatar = ? WHERE user_id = ?", (new_avatar, user_id))
      user_cookie['user_avatar'] = new_avatar

    db.commit()

    response.set_cookie("user", user_cookie, secret=os.getenv('COOKIE_SECRET'), httponly=True)
    return {"info": "Update succesful", "new_user_firstname": user_cookie["user_firstname"], "new_user_lastname": user_cookie["user_lastname"], "new_avatar": user_cookie["user_avatar"], "new_email": user_cookie["user_email"], "new_birthday": user_cookie["user_birthday"]}

  except Exception as ex:
    print("Put route error her", ex)
    return ex
  
  finally:
    print("Database closed")
    if "db" in locals(): db.close()



####### separate api #########



@put("/api-update-users-names")
def update():
  try:
    db = x.db()
    user_cookie = x.user()
    user_id = user_cookie["user_id"]
    user_firstname = user_cookie["user_firstname"]
    user_lastname = user_cookie["user_lastname"]
    
    new_user_firstname = x.update_user_firstname()
    if user_firstname != new_user_firstname and new_user_firstname != "" and new_user_firstname is not None:
      db.execute(f"UPDATE users SET user_firstname = ? WHERE user_firstname = ?", (new_user_firstname, user_firstname))
      user_cookie["user_firstname"] = new_user_firstname

    new_user_lastname = x.update_user_lastname()
    if user_lastname != new_user_lastname and new_user_lastname != "" and new_user_lastname is not None:
      db.execute(f"UPDATE users SET user_lastname = ? WHERE user_lastname = ?", (new_user_lastname, user_lastname))
      user_cookie["user_lastname"] = new_user_lastname

    db.commit()

    response.set_cookie("user", user_cookie, secret=os.getenv('COOKIE_SECRET'), httponly=True)
    return {"info": "Update succesful", "new_user_firstname": user_cookie["user_firstname"], "new_user_lastname": user_cookie["user_lastname"]}

  except Exception as ex:
    print("Put route error her", ex)
    return ex
  
  finally:
    print("Database closed")
    if "db" in locals(): db.close()


@put("/api-update-avatar")
def update():
  try:
    db = x.db()
    user_cookie = x.user()
    user_id = user_cookie["user_id"]
    
    avatar = user_cookie["user_avatar"]
    new_avatar = x.avatar_picture()
    if avatar != user_id and new_avatar != "" and new_avatar is not None:
      db.execute(f"UPDATE users SET user_avatar = ? WHERE user_id = ?", (new_avatar, user_id))
      user_cookie['user_avatar'] = new_avatar

    db.commit()

    response.set_cookie("user", user_cookie, secret=os.getenv('COOKIE_SECRET'), httponly=True)
    return {"info": "Update succesful", "new_avatar": user_cookie["user_avatar"]}

  except Exception as ex:
    print("Put route error her", ex)
    return ex
  
  finally:
    print("Database closed")
    if "db" in locals(): db.close()


@put("/api-update-email")
def update():
  try:
    db = x.db()
    user_cookie = x.user()
    user_id = user_cookie["user_id"]
    
    email = user_cookie["user_email"]
    new_email = x.validate_user_email()
    if email != user_id and new_email != "" and new_email is not None:
      db.execute(f"UPDATE users SET user_email = ? WHERE user_id = ?", (new_email, user_id))
      user_cookie['user_email'] = new_email

    db.commit()

    response.set_cookie("user", user_cookie, secret=os.getenv('COOKIE_SECRET'), httponly=True)
    return {"info": "Update succesful", "new_email": user_cookie["user_email"]}

  except Exception as ex:
    print("Put route error her", ex)
    return ex
  
  finally:
    print("Database closed")
    if "db" in locals(): db.close()

@put("/api-update-birthday")
def update():
  try:
    db = x.db()
    user_cookie = x.user()
    user_id = user_cookie["user_id"]
    
    birthday = user_cookie["user_birthday"]
    new_birthday = x.validate_user_birthday()
    if birthday != user_id and new_birthday != "" and new_birthday is not None:
      db.execute(f"UPDATE users SET user_birthday = ? WHERE user_id = ?", (new_birthday, user_id))
      user_cookie['user_birthday'] = new_birthday

    db.commit()

    response.set_cookie("user", user_cookie, secret=os.getenv('COOKIE_SECRET'), httponly=True)
    return {"info": "Update succesful", "new_birthday": user_cookie["user_birthday"]}

  except Exception as ex:
    print("Put route error her", ex)
    return ex
  
  finally:
    print("Database closed")
    if "db" in locals(): db.close()