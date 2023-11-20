from bottle import request
import sqlite3
import pathlib
##############################

def dict_factory(cursor, row):
    col_names = [col[0] for col in cursor.description]
    return {key: value for key, value in zip(col_names, row)}

###########################

def db():
    try:
        db = sqlite3.connect(
            str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
        db.execute("PRAGMA foreign_keys=ON")
        db.row_factory = dict_factory
        return db
    except Exception as e:
        print(e)
    finally:
        pass

##############################

# Validation of task

TASK_MIN_LEN = 1
TASK_MAX_LEN = 25
TASK_REGEX = "^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"


def validate_task(): 
    error = f"message min {TASK_MIN_LEN} max {TASK_MAX_LEN} characters"
    if len(request.forms.task_description) < TASK_MIN_LEN: raise Exception(error)
    if len(request.forms.task_description) > TASK_MAX_LEN: raise Exception(error)
    return request.forms.task_description
