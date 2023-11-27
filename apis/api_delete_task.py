from bottle import delete, request, response
import x

@delete('/api_delete_task')
def delete_task():
    try:
        db = x.db()
        task_id = request.forms.get("task_id", "")
        tasks = db.execute("SELECT * FROM tasks WHERE task_id = ?", (task_id,)).fetchall()
        if not tasks:
            raise Exception("Task not found")

        db.execute("DELETE FROM tasks WHERE task_id = ?", (task_id,))
        db.commit()
        return {'task_deleted': "ok"}

    except Exception as ex:
        response.status = 400
        return {'info': str(ex)}

    finally: 
        if 'db' in locals():
            db.close()
            