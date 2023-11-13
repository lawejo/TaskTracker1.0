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
