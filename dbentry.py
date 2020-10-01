import sqlite3 as sqlite3
from datetime import datetime
def dbinsert(data):
    try:
        db = sqlite3.connect('/home/pi/Desktop/flask_app/flaskapp/site.db') #DB connection
        cursor = db.cursor() #Create cursor object
        cursor.execute('''INSERT INTO reading(results,date_posted) VALUES(?,?)''', (data, datetime.now().strftime("%Y-%m-%d %H:%M:%S"),))
        db.commit()
    except Exception as e:
        raise e
    finally:
        db.close()
