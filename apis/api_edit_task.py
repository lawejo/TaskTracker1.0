from bottle import put, request, response
import x

@put('/api_edit_task/<task_id>')
def edit_task(task_id):
    try:
        db = x.db()

        # Retrieve task details from the request body
        task_title = request.forms.get("task_title")
        task_description = request.forms.get("task_description")
        task_due_date = request.forms.get("task_due_date")
        task_visibility = request.forms.get("task_visibility")

        # Check if the task exists
        task = db.execute("SELECT * FROM tasks WHERE task_id = ?", (task_id,)).fetchone()
        if not task:
            raise Exception("Task not found")

        # Update the task details
        db.execute(
            "UPDATE tasks SET task_title = ?, task_description = ?, task_due_date = ?, task_visibility = ? WHERE task_id = ?",
            (task_title, task_description, task_due_date, task_visibility, task_id)
        )

        db.commit()

        return {'info': 'Task updated successfully'}

    except Exception as ex:
        db.rollback()
        response.status = 400
        return {'info': str(ex)}

    finally:
        if 'db' in locals():
            db.close()
