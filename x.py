from bottle import request, response 
import os
import sqlite3
import pathlib
import re
from dotenv import load_dotenv

##############################
##### Cookie

# Load variables from .env file
load_dotenv()
COOKIE_SECRET = os.getenv("COOKIE_SECRET")

##############################
##### Database

def dict_factory(cursor, row):
    col_names = [col[0] for col in cursor.description]
    return {key: value for key, value in zip(col_names, row)}


def db():
    try:
        db = sqlite3.connect(
            str(pathlib.Path(__file__).parent.resolve())+"/TaskTracker.db")
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
##### Email address
EMAIL_AHREF = ''
try:
    import production
    EMAIL_AHREF = 'pythonanywhere'
except Exception as ex:
    print("Running local server")
    EMAIL_AHREF = "http://127.0.0.1:3000"


##############################
##### Validation of user inputs

USER_FIRSTNAME_MIN = 1
USER_FIRSTNAME_MAX = 50
USER_FIRSTNAME_REGEX = "^[a-zA-Z-9_]*$"

def validate_user_firstname():
    error = f"Firstname must {USER_FIRSTNAME_MIN} to {USER_FIRSTNAME_MAX} letters or numbers from 0 to 9"
    request.forms.user_firstname = request.forms.user_firstname.strip()
    if len(request.forms.user_firstname) < USER_FIRSTNAME_MIN:
        raise Exception(error)
    if len(request.forms.user_firstname) > USER_FIRSTNAME_MAX:
        raise Exception(error)
    if not re.match(USER_FIRSTNAME_REGEX, request.forms.user_firstname):
        raise Exception(error)
    return request.forms.user_firstname


USER_LASTNAME_MIN = 1
USER_LASTNAME_MAX = 50
USER_LASTNAME_REGEX = "^[a-zA-Z-9_]*$"

# english letter only and numbers from 0 to 9


def validate_user_lastname():
    error = f"Your lastname must {USER_LASTNAME_MIN} to {USER_LASTNAME_MAX} letters or numbers from 0 to 9. No spaces"
    request.forms.user_lastname = request.forms.user_lastname.strip()
    if len(request.forms.user_lastname) < USER_LASTNAME_MIN:
        raise Exception(error)
    if len(request.forms.user_lastname) > USER_LASTNAME_MAX:
        raise Exception(error)
    if not re.match(USER_LASTNAME_REGEX, request.forms.user_lastname):
        raise Exception(error)
    return request.forms.user_lastname


USER_EMAIL_MIN = 6
USER_EMAIL_MAX = 100
USER_EMAIL_REGEX = "^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"


def validate_user_email():
    error = f"Your email is invalid, it must be between {USER_EMAIL_MIN} and {USER_EMAIL_MAX}"
    request.forms.user_email = request.forms.user_email.strip()
    if len(request.forms.user_email) < USER_EMAIL_MIN:
        raise Exception(error)

    if len(request.forms.user_email) > USER_EMAIL_MAX:
        raise Exception(error)

    if not re.match(USER_EMAIL_REGEX, request.forms.user_email):
        raise Exception(error)
    return request.forms.user_email



USER_PASSWORD_MIN = 6
USER_PASSWORD_MAX = 50


def validate_user_password():
    error = f"Your password has to be {USER_PASSWORD_MIN} to {USER_PASSWORD_MAX} characters"
    user_password = request.forms.get("user_password", "")
    user_password = user_password.strip()
    request.forms.user_password = request.forms.user_password.strip()
    if len(user_password) < USER_PASSWORD_MIN:
        raise Exception(error)
    if len(user_password) > USER_PASSWORD_MAX:
        raise Exception(error)
    return user_password


def validate_user_confirm_password():
    error = f"Please make sure to write the same in both password fields"
    user_password = request.forms.get("user_password", "")
    user_confirm_password = request.forms.get("user_confirm_password", "")
    user_password = user_password.strip()
    user_confirm_password = user_confirm_password.strip()
    if user_confirm_password != user_password:
        raise Exception(error)
    return user_confirm_password
