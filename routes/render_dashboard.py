from bottle import get, template, response, request
import traceback
import x
import os


@get("/dashboard")
def show_tasks():
    try:
        db = x.db()  # Connect to your database
        
        
        user_cookie = x.get_cookie_user()

        if not user_cookie:
            return template('cookie-expired', user_cookie = user_cookie)
        todo = db.execute("SELECT * FROM tasks WHERE task_status = ?", ("todo",))
        todos = todo.fetchall()
        inprogress = db.execute("SELECT * FROM tasks WHERE task_status = ?", ("inprogress",))
        progtask = inprogress.fetchall()
        donetask = db.execute("SELECT * FROM tasks WHERE task_status = ?", ("done",))
        donetasks = donetask.fetchall()
   
    

        # Fetch tasks from the database
        cursor = db.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()

        cursor.close()
        x.set_headers()
        return template("dashboard", tasks=tasks, todos=todos, progtask=progtask, donetasks=donetasks, user_cookie=user_cookie)  # Pass tasks to your template for rendering
        
    except Exception as ex:
        response.status = 500  # Internal Server Error
        traceback.print_exc()  # Print the traceback for debugging
        return template('cookie-expired')

    finally:
        if "db" in locals():
            db.close()
