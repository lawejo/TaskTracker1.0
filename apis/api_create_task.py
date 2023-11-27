from bottle import post, request, response
import x
import uuid
import time
import sqlite3
import os

@post("/api_create_task")
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

        # Upload task image
        # picture_upload = request.files.get("task_image")
        # if not picture_upload.filename == "empty":
        #     name, ext = os.path.splitext(picture_upload.filename)
        #     if ext not in (".png", ".jpg", ".jpeg"):
        #         response.status = 400
        #         return "Picture not allowed"
        
        #     picture_name = str(uuid.uuid4().hex)
        #     picture_name = picture_name + ext
        #     picture_upload.save(f"picture_upload/{picture_name}")
        #     task_image = picture_name
        # else: 
        #     task_image = ""

        db.execute(
            "INSERT INTO tasks (task_id, task_created_at, task_title, task_description, task_due_date, task_visibility, task_image, task_assigned_users) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (task_id, task_created_at, task_title, task_description, task_due_date, task_visibility, task_image, 0)  # 0 for task_assigned_users initially
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
        }

    except Exception as ex:
        db.rollback()
        response.status = 400
        return {"info": str(ex)}

    finally:
        if "db" in locals():
            db.close()
