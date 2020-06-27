import sqlite3 as sqlite3

def dbinsert(data):
    try:
        db = sqlite3.connect('/home/pi/Desktop/flask_app/flaskapp/site.db') #DB connection
        cursor = db.cursor() #Create cursor object
        cursor.execute('''INSERT INTO reading(results) VALUES(?)''', (data,))
        db.commit()
    except Exception as e:
        raise e
    finally:
        db.close()
