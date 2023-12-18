from bottle import get, response, request
import x  

@get("/filter_task")
def filter_task():
    try:
        filter_tag = request.query.get("task_status")  # Retrieve the filter tag from URL query params

        if filter_tag not in ['todo', 'done', 'inprogress']:
            raise Exception(400, "Invalid filter tag")
        
        db = x.db()  

        filter_results = db.execute("SELECT * FROM tasks WHERE task_status = ?", (filter_tag,))

        # Fetch all rows and convert them to a list of dictionaries
        results = [dict(row) for row in filter_results.fetchall()]
        x.set_headers()
        return {"info": "ok", "results": results} 

    except Exception as ex:
        print(ex)
        try:
            response.status = ex.args[0]
            return {"info": ex.args[1]}
        except:
            response.status = 500
            return {"info": str(ex)}

    finally:
        if "db" in locals():
            db.close()
