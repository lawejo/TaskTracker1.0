from bottle import get, template, response, request
import traceback
import x


@get("/dashboard")
def show_tasks():
    try:
        db = x.db()  # Connect to your database
        
        # Fetch tasks from the database
        cursor = db.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        cursor.close()
        
        return template("dashboard", tasks=tasks)  # Pass tasks to your template for rendering
        
    except Exception as ex:
        response.status = 500  # Internal Server Error
        traceback.print_exc()  # Print the traceback for debugging
        return "An error occurred while fetching tasks."

    finally:
        if "db" in locals():
            db.close()
