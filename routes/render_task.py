from bottle import get, template, response, request
import traceback
import x  # Assuming x is where your database configuration and access is defined

@get("/task")
def show_tasks():
    try:
        db = x.db()  # Connect to your database
        
        # Fetch tasks from the database
        cursor = db.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        cursor.close()
        x.set_headers()
        return template("task", tasks=tasks)  # Pass tasks to your template for rendering
        
    except Exception as ex:
        response.status = 500  # Internal Server Error
        traceback.print_exc()  # Print the traceback for debugging
        return "An error occurred while fetching tasks."

    finally:
        if "db" in locals():
            db.close()
