from bottle import post, request, response
import x
import uuid
import time
import sqlite3
import os

@post("/api-create-task")
def create_task():
    try:
        db = x.db()

        task_id = str(uuid.uuid4().hex)
        task_created_at = int(time.time())
        task_title = request.forms.get("task_title")
        task_description = request.forms.get("task_description")
        task_due_date = request.forms.get("task_due_date")  # Should have a date instead 
        task_visibility = request.forms.get("task_visibility")
        task_image = ""
        task_status = request.forms.get("task_status")


        db.execute(
            "INSERT INTO tasks (task_id, task_created_at, task_title, task_description, task_due_date, task_visibility, task_image, task_assigned_users, task_status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (task_id, task_created_at, task_title, task_description, task_due_date, task_visibility, task_image, 0, task_status)
        )


        db.commit()

        return {
            "info": "ok",
            "task_id": task_id,
            "task_created_at": task_created_at,
            "task_title": task_title,
            "task_description": task_description,
            "task_due_date": task_due_date,
            "task_visibility": task_visibility,
            "task_image": task_image,
            "task_status": task_status
        }

    except Exception as ex:
        db.rollback()
        response.status = 400
        return {"info": str(ex)}

    finally:
        if "db" in locals():
            db.close()
